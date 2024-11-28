from .forms import MemberRegistrationForm
from django.db import connection
def register_view(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please check the details and try again.")
    else:
        form = MemberRegistrationForm()
    return render(request, 'members/register.html', {'form': form})


from django.contrib import messages

import hashlib

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Query to fetch the member based on the provided email
        with connection.cursor() as cursor:
            cursor.execute("SELECT MemberID, Name, PasswordHash, PasswordSalt FROM Members WHERE Email = %s", [email])
            result = cursor.fetchone()

        if result:
            member_id, name, password_hash, password_salt = result
            # Verify the password using the stored hash and salt
            password_hash_check = hashlib.pbkdf2_hmac('sha256', password.encode(), password_salt.encode(), 100000).hex()

            if password_hash_check == password_hash:
                # Store the MemberID in the session directly (Django's default session is still used to store it)
                request.session['user'] = member_id  # Storing the MemberID in session

                messages.success(request, f"Welcome back, {name}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid password.")
        else:
            messages.error(request, "No account found with this email.")

    return render(request, 'members/login.html')

from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import Member

# def home_view(request):
#     # Check if the user is logged in by checking the session
#     if 'user' in request.session:
#         member_id = request.session['user']
#         try:
#             # Retrieve the member using the session-stored ID
#             member = Member.objects.get(MemberID=member_id)
#             # Fetch member's bookings and invoices (assuming these are related models)
#             bookings = member.bookings.all()  # Example for fetching related bookings
#             invoices = member.invoices.all()  # Example for fetching related invoices
#             return render(request, 'members/home.html', {
#                 'member': member,
#                 'bookings': bookings,
#                 'invoices': invoices
#             })
#         except Member.DoesNotExist:
#             # Redirect to login if member does not exist in the database
#             return redirect('login')
#     else:
#         # If no user session exists, redirect to the login page
#         return redirect('login')  # Redirect to login if no session is found


from django.db import connection
from django.shortcuts import render, redirect
from .models import Member


def home_view(request):
    if 'user' in request.session:
        member_id = request.session['user']
        try:
            # Fetch the member details
            member = Member.objects.get(MemberID=member_id)

            # Fetch bookings directly from the database
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT b.BookingID, s.Name, b.StartTime, b.EndTime, b.Status
                    FROM Bookings b
                    JOIN Spaces s ON b.SpaceID = s.SpaceID
                    WHERE b.MemberID = %s
                """, [member_id])
                bookings = cursor.fetchall()  # List of tuples

            # Pass the data to the template
            return render(request, 'members/home.html', {
                'member': member,
                'bookings': bookings,
            })
        except Member.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages


@login_required
def create_booking(request):
    if request.method == 'POST':
        # Extract form data
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        space = request.POST.get('space')

        # Get the current member's ID
        member_id = request.user.member.MemberID

        # Raw SQL to insert a new booking
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Members_Booking (member_id, start_time, end_time, space)
            VALUES (%s, %s, %s, %s)
        """, [member_id, start_time, end_time, space])

        messages.success(request, "Booking created successfully!")
        return redirect('home')

    return render(request, 'members/create_booking.html')

from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages

def create_booking(request):
        return redirect('login')

        with connection.cursor() as cursor:
            cursor.execute("""


                with connection.cursor() as cursor:


from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages

    sort_by = request.GET.get('sort_by', 'hourly_price')  # Default sorting by hourly price
    sort_order = request.GET.get('sort_order', 'asc')  # Default ascending order

    # Validate sort order
    sort_order = 'ASC' if sort_order == 'asc' else 'DESC'

    # Fetch spaces with sorting
    query = f"""
        SELECT s.SpaceID, s.Name, p.hourly_price, p.monthly_price, p.weekly_price, p.yearly_price, s.OccupationStatus
        FROM Spaces s
        JOIN price p ON s.SpaceID = p.SpaceID
        WHERE s.OccupationStatus = 'Available'
        ORDER BY {sort_by} {sort_order}
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        spaces = cursor.fetchall()

    return render(request, 'members/coworking_spaces.html', {
        'spaces': spaces,
        'sort_by': sort_by,
        'sort_order': sort_order
    })
from django.http import HttpResponseRedirect

from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection

def book_space(request):
    if request.method == 'POST':
        # Retrieve data from the form
        space_id = request.POST.get('space_id')
        start_date = request.POST.get('start_date')  # Start Date (yyyy-mm-dd)
        start_time = request.POST.get('start_time')  # Start Time (HH:mm)
        end_date = request.POST.get('end_date')      # End Date (yyyy-mm-dd)
        end_time = request.POST.get('end_time')      # End Time (HH:mm)

        # Check if any required field is missing or empty
        if not start_date or not start_time or not end_date or not end_time:
            messages.error(request, "All fields (start date, start time, end date, end time) are required.")
            return redirect('book_space')  # Redirect back to the booking page

        try:
            start_datetime = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")
            end_datetime = datetime.strptime(f"{end_date} {end_time}", "%Y-%m-%d %H:%M")

        except ValueError:
            # If the date and time format is incorrect, show an error
            messages.error(request, "Please provide valid date and time formats.")
            return redirect('book_space')

        # Get the MemberID from the session
        member_id = request.session.get('user')

        if not member_id:
            messages.error(request, "You must be logged in to book a space.")
            return redirect('login')

        # Check if the space is available for the given time range
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*) FROM Bookings
                WHERE SpaceID = %s
                AND Status = 'Booked'
                AND (
                )
            """, [space_id, start_datetime, start_datetime, end_datetime, end_datetime])
            count = cursor.fetchone()[0]

            if count > 0:
                messages.error(request, "This space is already booked for the selected time.")
                return redirect('book_space')

            # Proceed with booking the space
            try:
                cursor.execute("""
                    VALUES (%s, %s, %s, %s, 'Booked')
                """, [member_id, space_id, start_datetime, end_datetime])

                # Update the space's occupation status
                cursor.execute("""
                    UPDATE Spaces
                    SET OccupationStatus = 'Booked'
                    WHERE SpaceID = %s
                """, [space_id])

                messages.success(request, "Booking created successfully!")
                return redirect('home')  # Redirect back to the home page after booking
            except Exception as e:
                messages.error(request, f"Error booking space: {str(e)}")
                return redirect('book_space')

    # Get available spaces to display on the booking page
    with connection.cursor() as cursor:
        cursor.execute("""
            FROM Spaces s
            JOIN price p ON s.SpaceID = p.SpaceID
            WHERE s.OccupationStatus = 'Available'
        """)
        spaces = cursor.fetchall()

    return render(request, 'members/book_space.html', {'spaces': spaces})
