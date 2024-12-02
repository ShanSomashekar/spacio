from django.http import HttpResponse
from django.urls import reverse
from .forms import MemberRegistrationForm
from django.db import connection

def register_view(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            member = form.save()

            # Optionally, log or print the saved data for debugging
            print(f"Member {member.first_name} {member.last_name} saved with ID: {member.id}")

            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        else:
            # If the form is invalid, print or log the errors
            print("Form errors:", form.errors)
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
                return redirect('members:home')
            else:
                messages.error(request, "Invalid password.")
        else:
            messages.error(request, "No account found with this email.")

    return render(request, 'members/login.html')



from .models import Member  # Ensure your Member model is imported

def home_view(request):
    if 'user' in request.session:
        member_id = request.session['user']
        try:
            # Fetch the member details
            member = Member.objects.get(MemberID=member_id)

            # Fetch bookings and invoices together, linked by BookingID
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        b.BookingID, s.Name AS Space, b.StartTime, b.EndTime, b.Status,
                        i.InvoiceID, i.Amount, i.Status AS InvoiceStatus, i.IssueDate
                    FROM 
                        Bookings b
                    JOIN 
                        Spaces s ON b.SpaceID = s.SpaceID
                    LEFT JOIN 
                        Invoices i ON b.BookingID = i.BookingID
                    WHERE 
                        b.MemberID = %s
                """, [member_id])
                bookings = cursor.fetchall()

            # Calculate total hours booked this month (MariaDB/MySQL compatible)
            current_month = datetime.now().month
            current_year = datetime.now().year
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT COALESCE(SUM(
                        TIMESTAMPDIFF(HOUR, b.StartTime, b.EndTime)
                    ), 0) AS total_hours
                    FROM Bookings b
                    WHERE b.MemberID = %s 
                        AND MONTH(b.StartTime) = %s 
                        AND YEAR(b.StartTime) = %s
                """, [member_id, current_month, current_year])
                total_hours = round(cursor.fetchone()[0], 2)

            # Fetch favorite spaces (top 3 most booked spaces)
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT s.Name, COUNT(b.BookingID) AS booking_count
                    FROM Bookings b
                    JOIN Spaces s ON b.SpaceID = s.SpaceID
                    WHERE b.MemberID = %s
                    GROUP BY s.Name
                    ORDER BY booking_count DESC
                    LIMIT 3
                """, [member_id])
                favorite_spaces = cursor.fetchall()

            # Fetch booking trends (bookings per day)
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT DATE(b.StartTime) AS booking_date, COUNT(*) AS booking_count
                    FROM Bookings b
                    WHERE b.MemberID = %s
                    GROUP BY booking_date
                    ORDER BY booking_date ASC
                """, [member_id])
                booking_trends = cursor.fetchall()

            # Pass all the data to the template
            return render(request, 'members/home.html', {
                'member': member,
                'bookings': bookings,
                'total_hours': total_hours,
                'favorite_spaces': favorite_spaces,
                'booking_trends': booking_trends,
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

from django.contrib.auth.decorators import login_required



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
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        space = request.POST.get('space')

        member_id = request.session.get('user')

        if not member_id:
            messages.error(request, "You must be logged in to create a booking.")
            return redirect('login')

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Bookings (MemberID, StartTime, EndTime, SpaceID)
                VALUES (%s, %s, %s, %s)
            """, [member_id, start_time, end_time, space])

        messages.success(request, "Booking created successfully!")
        return redirect('home')

    # Fetch available spaces
    with connection.cursor() as cursor:
        cursor.execute("SELECT SpaceID, Name FROM Spaces WHERE OccupationStatus = 'Available'")
        spaces = cursor.fetchall()

    return render(request, 'members/create_booking.html', {'spaces': spaces})



def coworking_spaces(request):
    # Get filter and sorting parameters from the request
    sort_by = request.GET.get('sort_by', 'HourlyPrice')
    sort_order = request.GET.get('sort_order', 'asc')
    space_type = request.GET.get('space_type', None)
    start_time = request.GET.get('start_time', None)
    end_time = request.GET.get('end_time', None)

    # Validate sort_by column to prevent SQL injection
    valid_sort_columns = ['HourlyPrice', 'DailyPrice', 'MonthlyPrice', 'YearlyPrice']
    if sort_by not in valid_sort_columns:
        sort_by = 'HourlyPrice'

    # Query for all available space types
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT Type FROM Spaces")
        space_types = [row[0] for row in cursor.fetchall()]

    # Construct the main SQL query for spaces
    sql = f"""
        SELECT 
            s.SpaceID, 
            s.Name, 
            s.Type, 
            s.Capacity,
            p.HourlyPrice, 
            p.DailyPrice, 
            p.MonthlyPrice, 
            p.YearlyPrice, 
            s.OccupationStatus
        FROM Spaces s
        JOIN price p ON s.SpaceID = p.SpaceID
        WHERE s.OccupationStatus = 'Available'
    """
    params = []

    # Apply space type filter
    if space_type:
        sql += " AND s.Type = %s"
        params.append(space_type)

    # Exclude booked spaces during the specified time
    if start_time and end_time:
        sql += """
            AND s.SpaceID NOT IN (
                SELECT SpaceID
                FROM Bookings
                WHERE StartTime < %s AND EndTime > %s
            )
        """
        params.extend([end_time, start_time])

    # Apply sorting
    sql += f" ORDER BY {sort_by} {'ASC' if sort_order == 'asc' else 'DESC'}"

    # Execute the main query
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        spaces = cursor.fetchall()

    # Render the template with data
    return render(request, 'members/coworking_spaces.html', {
        'spaces': spaces,
        'space_types': space_types,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'space_type': space_type,
        'start_time': start_time,
        'end_time': end_time,
    })



from django.shortcuts import render, HttpResponse

from datetime import datetime, timedelta
# @login_required()
def book_space(request, SpaceID):
    if 'user' in request.session:
        member_id = request.session['user']

    if request.method == 'POST':
        # Extract start and end datetime from form
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')

        try:
            # Convert the datetime strings to datetime objects
            start_datetime = datetime.fromisoformat(start_time_str)
            end_datetime = datetime.fromisoformat(end_time_str)
        except ValueError as e:
            return HttpResponse(f"Invalid datetime format: {e}", status=400)

        # Fetch space details using raw SQL
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT S.SpaceID, S.Name, p.HourlyPrice, p.DailyPrice, p.MonthlyPrice, p.YearlyPrice
                FROM Spaces S 
                JOIN price p ON S.SpaceID = p.SpaceID
                WHERE S.SpaceID = %s
            """, [SpaceID])
            space = cursor.fetchone()

        if space:
            # Extract space details
            space_id = space[0]
            space_name = space[1]
            hourly_rate = space[2]
            daily_rate = space[3]
            monthly_rate = space[4]

            # Calculate the price based on the duration
            total_price = calculate_price(start_datetime, end_datetime, hourly_rate, daily_rate, monthly_rate)
            tax_amount = Decimal(total_price) * Decimal(0.18)  # 18% tax
            additional_fees = 100  # Flat additional fee
            total = total_price + additional_fees + tax_amount
            status = 'Payment Pending'
            # Confirm booking - Insert booking into the database


            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Bookings (SpaceID, MemberID, StartTime, EndTime)
                    VALUES (%s, %s, %s, %s)
                """, [space_id, member_id, start_datetime, end_datetime])
                cursor.execute("SELECT LAST_INSERT_ID()")
                BookingID = cursor.fetchone()[0]

                cursor.execute("""
                        INSERT INTO Invoices (BookingID, IssueDate, DueDate, Amount, TaxAmount, AdditionalFees, total, Status)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, [BookingID,  datetime.now(), ( datetime.now() + timedelta(days=7)), total_price,  tax_amount, additional_fees, total, status])


            # Return confirmation page or redirect
            return redirect(reverse('members:booking_confirmation', args=[BookingID]))

    else:
        # GET request: Fetch space details and show the booking form
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT SpaceID, Name
                FROM Spaces
                WHERE SpaceID = %s
            """, [SpaceID])
            space = cursor.fetchone()

        if space:
            return render(request, 'members/book_space.html', {'space': space})
        else:
            return HttpResponse("Space not found", status=404)


from decimal import Decimal

def calculate_price(start_datetime, end_datetime, hourly_rate, daily_rate, monthly_rate):
    """
    Calculate the price for the space based on the duration of the booking.
    """
    duration = end_datetime - start_datetime
    hours = duration.total_seconds() / 3600  # Convert to hours

    # Convert hours (float) to Decimal for accurate calculations
    hours = Decimal(hours)

    if hours < 24:
        # Price for hourly booking
        return hourly_rate * hours
    elif 24 <= hours < 744:  # 24 hours * 31 days = 744 hours (approximately one month)
        # Price for daily booking
        days = hours / Decimal(24)  # Convert days to Decimal
        return daily_rate * days
    else:
        # Price for monthly booking
        return monthly_rate



    from django.shortcuts import render
    from django.db import connection

from django.db import connection
from django.shortcuts import render

def booking_confirmation(request, booking_id):
    cursor = connection.cursor()

    # Execute the SQL query to fetch booking and invoice details
    cursor.execute("""
        SELECT 
            b.BookingID AS booking_id,
            b.StartTime,
            b.EndTime,
            s.name AS space_name,
            i.IssueDate,
            i.DueDate,
            i.Amount,
            i.TaxAmount,
            i.AdditionalFees,
            i.Status,
            i.total
        FROM 
            Bookings b
        JOIN 
            Spaces s ON b.SpaceID = s.SpaceID
        JOIN 
            Invoices i ON b.BookingID = i.BookingID
        WHERE 
            b.BookingID = %s
    """, [booking_id])

    # Fetch the result
    booking_data = cursor.fetchone()

    if booking_data:
        # Convert the result into a dictionary for easy access in the template
        booking_details = {
            'booking_id': booking_data[0],
            'start_time': booking_data[1],
            'end_time': booking_data[2],
            'space_name': booking_data[3],
            'issue_date': booking_data[4],
            'due_date': booking_data[5],
            'amount': booking_data[6],
            'tax_amount': booking_data[7],
            'additional_fees': booking_data[8],
            'status': booking_data[9],
            'total': booking_data[10],
        }

        return render(request, 'members/booking_confirmation.html', {'booking_details': booking_details})
    else:
        return HttpResponse("Booking not found", status=404)

