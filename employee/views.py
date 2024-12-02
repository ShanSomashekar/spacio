from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
import hashlib
import os
from mysite import settings
from django.contrib.auth.decorators import login_required

# Helper function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Helper function to generate a new password hash and salt
def generate_password_hash_and_salt(password):
    salt = os.urandom(16).hex()  # Generate a new salt
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000).hex()  # Hash the password
    return password_hash, salt

# Create a new employee
def create_employee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST.get('phone_number', None)
        position = request.POST['position']
        department = request.POST.get('department', None)
        hire_date = request.POST['hire_date']
        salary = request.POST.get('salary', None)
        temp_password = request.POST['temp_password']  # Temporary password
        must_change_password = True  # Always set to True initially

        # Generate password hash and salt for the temporary password
        password_hash, password_salt = generate_password_hash_and_salt(temp_password)

        # Insert new employee into the database
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Employees (
                    FirstName, LastName, Email, PhoneNumber, Position, Department, 
                    HireDate, Salary, PasswordHash, PasswordSalt, MustChangePassword, TempPassword
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, [
                first_name, last_name, email, phone_number, position, department,
                hire_date, salary, password_hash, password_salt, must_change_password, temp_password
            ])
        messages.success(request, "Employee created successfully!")
        return redirect('create_employee')

    return render(request, 'employee/create_employee.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
import hashlib


from django.shortcuts import redirect
from django.contrib import messages
import hashlib
from django.db import connection

def employee_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Query to fetch the user by email using raw SQL
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT EmployeeID, FirstName, PasswordHash, PasswordSalt, MustChangePassword, TempPassword FROM Employees WHERE email = %s",
                [email])
            result = cursor.fetchone()

        if result:
            user_id, name, password_hash, password_salt, must_change_password, temp_password = result

            # Check if the user must change the password (first-time login)
            if must_change_password == 1:
                # Compare the provided password with the TempPassword
                if password == temp_password:
                    # If the password matches the TempPassword, log the user in
                    request.session['employee_id'] = user_id  # Store employee_id in session
                    request.session['must_change_password'] = True  # Set password change flag
                    messages.info(request, "You need to change your password.")

                    # Redirect to change password page
                    next_url = request.GET.get('next', '/employee/change_password/')
                    return redirect(next_url)
                else:
                    messages.error(request, "Incorrect temporary password.")
            else:
                # If the user doesn't need to change the password, check the hashed password
                password_hash_check = hashlib.pbkdf2_hmac('sha256', password.encode(), password_salt.encode(),
                                                          100000).hex()

                if password_hash_check == password_hash:
                    # If password is correct, log the user in
                    request.session['employee_id'] = user_id  # Store employee_id in session
                    request.session['must_change_password'] = False  # Password changed, no need to enforce

                    messages.success(request, f"Welcome back, {name}!")

                    # Redirect to dashboard or the 'next' URL if provided
                    next_url = request.GET.get('next', '/employee/dashboard/')  # Default to dashboard
                    return redirect(next_url)
                else:
                    messages.error(request, "Invalid password.")
        else:
            messages.error(request, "No account found with this email.")

    return render(request, 'employee/login.html')


# Change password view
# @login_required(login_url=settings.LOGIN_URL_EMPLOYEES)
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Get the currently logged-in employee's ID from the session
        employee_id = request.session.get('user_id')

        if not employee_id:
            messages.error(request, "You must be logged in to change your password.")
            return redirect('login')

        # Fetch the current password hash, salt, and TempPassword from the database
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT PasswordHash, PasswordSalt, TempPassword, MustChangePassword
                FROM Employees 
                WHERE EmployeeID = %s
            """, [employee_id])
            result = cursor.fetchone()

        if not result:
            messages.error(request, "Employee not found.")
            return redirect('login')

        current_hash, current_salt, temp_password, must_change_password = result

        # Verify the old password (if it's not the temp password)
        if must_change_password == 1:  # First-time login with temp password
            if old_password != temp_password:
                messages.error(request, "Old password is incorrect.")
                return redirect('change_password')
        else:
            # Check if the old password matches the stored password hash
            old_password_hash_check = hashlib.pbkdf2_hmac(
                'sha256',
                old_password.encode(),
                current_salt.encode(),
                100000
            ).hex()

            if old_password_hash_check != current_hash:
                messages.error(request, "Old password is incorrect.")
                return redirect('change_password')

        # Check if the new password matches the confirmation
        if new_password != confirm_password:
            messages.error(request, "New password and confirmation do not match.")
            return redirect('change_password')

        # Generate a new salt and hash the new password
        new_salt = os.urandom(16).hex()
        new_password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            new_password.encode(),
            new_salt.encode(),
            100000
        ).hex()

        # Update the password in the database and set MustChangePassword to 0
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE Employees 
                SET PasswordHash = %s, PasswordSalt = %s, MustChangePassword = 0, TempPassword = NULL
                WHERE EmployeeID = %s
            """, [new_password_hash, new_salt, employee_id])

        messages.success(request, "Your password has been successfully updated.")
        return redirect('employee_dashboard')  # Or redirect to another page as needed

    return render(request, 'employee/change_password.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url=settings.LOGIN_URL_EMPLOYEES)
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages

from django.shortcuts import render, redirect
from django.db import connection

from django.shortcuts import render, redirect
from django.db import connection
from datetime import date, timedelta

from datetime import datetime
from django.shortcuts import render, redirect
from django.db import connection

from datetime import datetime
from django.shortcuts import render, redirect
from django.db import connection

from datetime import datetime
from django.shortcuts import render, redirect
from django.db import connection

def employee_dashboard(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('/employee/login/?next=/employee/dashboard/')

    # Fetch employee details
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT FirstName, LastName, Email 
            FROM Employees 
            WHERE EmployeeID = %s
        """, [employee_id])
        employee = cursor.fetchone()

    if not employee:
        return redirect('/employee/login/?next=/employee/dashboard/')

    employee_data = {
        'first_name': employee[0],
        'last_name': employee[1],
        'email': employee[2],
    }

    today = datetime.today().date()

    # Fetch spaces in use today and not in use today
    spaces_in_use_today = []
    spaces_not_in_use_today = []

    # Fetch today's bookings
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.Name, b.StartTime, b.EndTime, b.Status, b.SpaceID
            FROM Bookings b
            JOIN Spaces s ON b.SpaceID = s.SpaceID
            WHERE DATE(b.StartTime) = CURDATE()
        """)
        todays_bookings = cursor.fetchall()

        # Get all space IDs that are booked today
        booked_space_ids = [booking[4] for booking in todays_bookings]

    # Fetch all spaces
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT SpaceID, Name 
            FROM Spaces
        """)
        all_spaces = cursor.fetchall()

    # Separate spaces into those in use today and those not in use
    for space in all_spaces:
        if space[0] in booked_space_ids:
            spaces_in_use_today.append(space[1])
        else:
            spaces_not_in_use_today.append(space[1])

    # Fetch total revenue for today
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT SUM(Amount) 
            FROM Invoices
            WHERE DATE(IssueDate) = CURDATE()
        """)
        total_revenue = cursor.fetchone()[0] or 0

    # Fetch total revenue for the current month
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT SUM(Amount)
            FROM Invoices
            WHERE YEAR(IssueDate) = YEAR(CURDATE()) AND MONTH(IssueDate) = MONTH(CURDATE())
        """)
        monthly_revenue = cursor.fetchone()[0] or 0

    # Fetch total revenue for the current quarter
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT SUM(Amount)
            FROM Invoices
            WHERE YEAR(IssueDate) = YEAR(CURDATE()) AND QUARTER(IssueDate) = QUARTER(CURDATE())
        """)
        quarterly_revenue = cursor.fetchone()[0] or 0

    # Fetch total revenue for the current year
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT SUM(Amount)
            FROM Invoices
            WHERE YEAR(IssueDate) = YEAR(CURDATE())
        """)
        yearly_revenue = cursor.fetchone()[0] or 0

    # Fetch payment status (Paid vs Unpaid)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT SUM(Amount)
            FROM Invoices
            WHERE Status = 'Paid' AND YEAR(IssueDate) = YEAR(CURDATE())
        """)
        paid_revenue = cursor.fetchone()[0] or 0

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT SUM(Amount)
            FROM Invoices
            WHERE Status = 'Unpaid' AND YEAR(IssueDate) = YEAR(CURDATE())
        """)
        unpaid_revenue = cursor.fetchone()[0] or 0

    # Revenue per Space Type (for the current month)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.Type, SUM(i.Amount)
            FROM Invoices i
            JOIN Bookings b ON i.BookingID = b.BookingID
            JOIN Spaces s ON b.SpaceID = s.SpaceID
            WHERE MONTH(i.IssueDate) = MONTH(CURDATE()) AND YEAR(i.IssueDate) = YEAR(CURDATE())
            GROUP BY s.Type
        """)
        revenue_by_space_type = cursor.fetchall()

    context = {
        'employee': employee_data,
        'todays_bookings': todays_bookings,
        'total_revenue': total_revenue,
        'monthly_revenue': monthly_revenue,
        'quarterly_revenue': quarterly_revenue,
        'yearly_revenue': yearly_revenue,
        'paid_revenue': paid_revenue,
        'unpaid_revenue': unpaid_revenue,
        'revenue_by_space_type': revenue_by_space_type,
        'spaces_in_use_today': spaces_in_use_today,
        'spaces_not_in_use_today': spaces_not_in_use_today,
    }

    return render(request, 'employee/employee_dashboard.html', context)


def employee_logout(request):
    # Clear the session data (log out the employee)
    if 'user_id' in request.session:
        del request.session['user_id']  # Remove the user_id from the session
        messages.success(request, "You have been logged out successfully.")

    # Redirect to the login page or homepage
    return redirect('employee_login')  # Or redirect to any other page like homepage or dashboard

from django.contrib.auth.views import LogoutView

class EmployeeLogoutView(LogoutView):
    next_page = '/employee/login/'