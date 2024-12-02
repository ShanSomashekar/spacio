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
                    request.session['user_id'] = user_id  # Store user_id in session
                    messages.info(request, "You need to change your password.")

                    # Get the 'next' parameter to redirect to the correct page after login
                    next_url = request.GET.get('next', '/employee/change_password/')
                    return redirect(next_url)  # Redirect to change password page
                else:
                    messages.error(request, "Incorrect temporary password.")
            else:
                # If the user doesn't need to change the password, check the hashed password
                password_hash_check = hashlib.pbkdf2_hmac('sha256', password.encode(), password_salt.encode(),
                                                          100000).hex()

                if password_hash_check == password_hash:
                    # If password is correct, log the user in
                    request.session['user_id'] = user_id  # Store user_id in session
                    messages.success(request, f"Welcome back, {name}!")

                    # Get the 'next' parameter to redirect after successful login
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
from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection


def employee_dashboard(request):
    # Get the logged-in user's ID
    user_id = request.user.id

    # 1. Get employee-specific data using raw SQL
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT FirstName, LastName, Email, Position
            FROM Employees
            WHERE EmployeeID = %s
        """, [user_id])
        employee_data = cursor.fetchone()

    if not employee_data:
        # If no employee data found for the user, redirect to login or error page
        return redirect('login')

    employee = {
        'first_name': employee_data[0],
        'last_name': employee_data[1],
        'email': employee_data[2],
        'position': employee_data[3]
    }

    # 2. Get the spaces booked for today
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT s.name, b.start_time, b.end_time, b.status
            FROM bookings b
            JOIN spaces s ON b.space_id = s.id
            WHERE b.start_time >= CURDATE() AND b.start_time < CURDATE() + INTERVAL 1 DAY
        """)
        todays_bookings = cursor.fetchall()

    # 3. Get the total revenue and revenue breakdown by space
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT SUM(i.amount) AS total_revenue
            FROM invoices i
            JOIN bookings b ON i.booking_id = b.id
            WHERE i.issue_date >= CURDATE() AND i.issue_date < CURDATE() + INTERVAL 1 DAY
        """)
        total_revenue = cursor.fetchone()[0]

        cursor.execute("""
            SELECT s.name, SUM(i.amount) AS revenue
            FROM invoices i
            JOIN bookings b ON i.booking_id = b.id
            JOIN spaces s ON b.space_id = s.id
            WHERE i.issue_date >= CURDATE() AND i.issue_date < CURDATE() + INTERVAL 1 DAY
            GROUP BY s.name
        """)
        revenue_by_space = cursor.fetchall()

    # 4. Get active members for this month
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT COUNT(DISTINCT b.member_id)
            FROM bookings b
            WHERE b.start_time >= CURDATE() - INTERVAL 1 MONTH
        """)
        active_members = cursor.fetchone()[0]

    # 5. Get member retention (new vs returning)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                COUNT(DISTINCT CASE WHEN b.start_time <= CURDATE() - INTERVAL 1 MONTH THEN b.member_id END) AS new_members,
                COUNT(DISTINCT CASE WHEN b.start_time > CURDATE() - INTERVAL 1 MONTH THEN b.member_id END) AS returning_members
            FROM bookings b
            WHERE b.start_time >= CURDATE() - INTERVAL 1 YEAR
        """)
        member_retention = cursor.fetchone()

    # 6. Get booking trends (bookings per day)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT DATE(b.start_time) AS date, COUNT(b.id) AS bookings_count
            FROM bookings b
            WHERE b.start_time >= CURDATE() - INTERVAL 1 MONTH
            GROUP BY DATE(b.start_time)
            ORDER BY DATE(b.start_time)
        """)
        booking_trends = cursor.fetchall()

    # 7. Get invoice status (paid vs unpaid)
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                SUM(CASE WHEN i.status = 'Paid' THEN i.amount ELSE 0 END) AS paid_revenue,
                SUM(CASE WHEN i.status = 'Unpaid' THEN i.amount ELSE 0 END) AS unpaid_revenue
            FROM invoices i
            WHERE i.issue_date >= CURDATE() - INTERVAL 1 MONTH
        """)
        invoice_status = cursor.fetchone()

    # Context for rendering
    context = {
        'employee': employee,
        'todays_bookings': todays_bookings,
        'total_revenue': total_revenue,
        'revenue_by_space': revenue_by_space,
        'active_members': active_members,
        'member_retention': member_retention,
        'booking_trends': booking_trends,
        'invoice_status': invoice_status,
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