# from django.shortcuts import render, get_object_or_404, redirect
# from django.db import connection
# from .models import *
# from .forms import SpaceForm, PricePlanForm, BookingForm, MemberForm, AccessControlForm, MembershipForm, InvoiceForm, PaymentForm, FeedbackForm, EventForm
#
#
def view_tables(request):
    """
    View to list all tables in the database.
    """
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]  # List of table names

    return render(request, 'view/tables.html', {"tables": tables})
#
#
# def list_records(request, table_name):
#     """
#     List all records from the specified table, with dynamic ID assignment if necessary.
#     """
#     with connection.cursor() as cursor:
#         try:
#             # Fetch all rows from the table
#             cursor.execute(f"SELECT * FROM `{table_name}`")
#             rows = cursor.fetchall()
#             columns = [col[0] for col in cursor.description]  # Extract column names
#
#             # Dynamically assign an ID if the table doesn't have an 'id' column
#             if "id" not in columns:
#                 rows = [{"id": idx + 1, **dict(zip(columns, row))} for idx, row in enumerate(rows)]
#                 columns.insert(0, "id")  # Add 'id' to the column list
#             else:
#                 rows = [dict(zip(columns, row)) for row in rows]  # Convert rows to dictionaries
#         except Exception as e:
#             rows = []
#             columns = []
#             error = str(e)
#             return render(request, 'view/error.html', {"error": error})
#
#     return render(request, 'view/list_records.html', {"rows": rows, "columns": columns, "table_name": table_name})
#


def list_records(request, table_name):
    """
    List all records from the specified table, with dynamic ID assignment if necessary.
    """
    def get_primary_key_column(table_name):
        """Fetch the primary key column for the given table."""
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY'")
            result = cursor.fetchone()
            return result[4] if result else None  # Column name is in the 5th index (index 4)

    with connection.cursor() as cursor:
        try:
            # Fetch all rows from the table
            cursor.execute(f"SELECT * FROM `{table_name}`")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]  # Extract column names

            # Dynamically identify the primary key column
            primary_key_column = get_primary_key_column(table_name)
            if not primary_key_column:
                raise Exception(f"No primary key found for table {table_name}")

            # Convert rows to dictionaries with primary key explicitly included
            rows = [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            rows = []
            columns = []
            error = str(e)
            return render(request, 'view/error.html', {"error": error})

    return render(request, 'view/list_records.html', {
        "rows": rows,
        "columns": columns,
        "table_name": table_name,
        "primary_key_column": primary_key_column,  # Pass primary key column
        "total_records": len(rows),
        "has_next": False,  # Update based on pagination logic
        "has_previous": False,  # Update based on pagination logic
    })


from django.http import HttpResponse


def add_record(request, table_name):
    if request.method == 'POST':
        # Get columns from the form
        columns = get_columns_for_table(table_name)

        # Prepare the data to insert
        values = []
        for column in columns:
            value = request.POST.get(column)  # Get the value for each column
            if value is None:  # Check if any field is missing
                return HttpResponse(f"Error: Missing value for column '{column}'", status=400)
            values.append(value)

        # Generate placeholders for the query
        placeholders = ', '.join(['%s'] * len(columns))  # Example: '%s, %s, %s'
        column_names = ', '.join(columns)  # Example: 'name, location, capacity'

        # Insert the data into the table using raw SQL
        with connection.cursor() as cursor:
            query = f"""
                INSERT INTO {table_name} ({column_names})
                VALUES ({placeholders});
            """
            cursor.execute(query, values)

        # Redirect to the list view after adding the record
        return redirect(f'/view/{table_name}/list/')

    # If it's a GET request, render the form
    columns = get_columns_for_table(table_name)

    return render(request, 'view/add_record.html', {
        'table_name': table_name,
        'columns': columns
    })


def get_columns_for_table(table_name):
    """Helper function to get column names for a given table"""
    with connection.cursor() as cursor:
        cursor.execute(f"DESCRIBE {table_name};")
        columns = [row[0] for row in cursor.fetchall()]
    return columns


# Edit record view

from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from django.http import Http404
from django import forms
from django.contrib import messages

from django.shortcuts import render, redirect
from django.db import connection

def edit_record(request, table_name, id):
    def get_columns_for_table(table_name):
        """Retrieve all columns for the given table."""
        with connection.cursor() as cursor:
            cursor.execute(f"DESCRIBE {table_name}")
            return [column[0] for column in cursor.fetchall()]

    def get_record(table_name, primary_key_column, id):
        """Fetch a single record by its primary key."""
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name} WHERE {primary_key_column} = %s", [id])
            return cursor.fetchone()

    def get_primary_key_column(table_name):
        """Get the primary key column for the given table."""
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY'")
            result = cursor.fetchone()
            return result[4] if result else None  # Column name is in the 5th index (index 4)

    # Get primary key column dynamically
    primary_key_column = get_primary_key_column(table_name)
    if not primary_key_column:
        return render(request, 'view/error.html', {'message': f"Primary key not found for table {table_name}"})

    # Get table columns
    columns = get_columns_for_table(table_name)

    if request.method == 'POST':
        # Handle form submission to update the record
        update_query = f"UPDATE {table_name} SET " + ", ".join([f"{col} = %s" for col in columns])
        update_query += f" WHERE {primary_key_column} = %s"

        # Collect new values from the form
        values = [request.POST[col] for col in columns]
        values.append(id)  # Add the primary key value for the WHERE clause

        # Execute the update query
        with connection.cursor() as cursor:
            cursor.execute(update_query, values)

        # Redirect to the list page after successful update
        return redirect('list_records', table_name=table_name)

    else:
        # Fetch the record to pre-fill the form
        record = get_record(table_name, primary_key_column, id)
        if not record:
            return render(request, 'view/error.html', {'message': f"Record not found for {primary_key_column} = {id}"})

        # Convert the record to a dictionary (column names as keys)
        record_dict = dict(zip(columns, record))

        # Render the edit form with pre-filled values
        return render(request, 'view/edit_record.html', {
            'table_name': table_name,
            'columns': columns,
            'record': record_dict,
            'primary_key_column': primary_key_column  # Pass primary key column to the template
        })
def delete_record(request, table_name, id):
    def get_primary_key_column(table_name):
        """Fetch the primary key column for the given table."""
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW KEYS FROM {table_name} WHERE Key_name = 'PRIMARY'")
            result = cursor.fetchone()
            return result[4] if result else None  # Column name is in the 5th index (index 4)

    # Fetch the primary key column name
    primary_key_column = get_primary_key_column(table_name)
    if not primary_key_column:
        return render(request, 'error.html', {'message': f"Primary key not found for table {table_name}"})

    if request.method == 'POST':
        # Delete the record from the table
        delete_query = f"DELETE FROM {table_name} WHERE {primary_key_column} = %s"

        with connection.cursor() as cursor:
            cursor.execute(delete_query, [id])

        # Redirect to the list page after successful deletion
        return redirect('list_records', table_name=table_name)

    else:
        # If not a POST request, show a confirmation page
        return render(request, 'view/confirm_delete.html', {
            'table_name': table_name,
            'record_id': id,
            'primary_key_column': primary_key_column  # Pass primary key column to the template
        })


