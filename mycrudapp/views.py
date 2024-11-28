# from django.shortcuts import render, redirect
# from django.db import connection
# from django.http import HttpResponse
# from . import sql_operations
#
#
# # Home Page to List All Tables
# def home(request):
#     # Get all table names in the database
#     tables = get_all_tables()
#     return render(request, 'home.html', {'tables': tables})
#
#
# # Function to fetch all table names in the database
# def get_all_tables():
#     with connection.cursor() as cursor:
#         cursor.execute("SHOW TABLES")
#         tables = [row[0] for row in cursor.fetchall()]
#     return tables
#
#
# # Table View - List all rows and columns of a selected table
# def table_view(request, table_name):
#     columns, rows = get_table_data(table_name)
#     return render(request, 'table_view.html', {'columns': columns, 'rows': rows, 'table_name': table_name})
#
#
# # Function to fetch rows and columns of a specific table
# def get_table_data(table_name):
#     with connection.cursor() as cursor:
#         cursor.execute(f"DESCRIBE {table_name}")
#         columns = [row[0] for row in cursor.fetchall()]  # Get column names
#         cursor.execute(f"SELECT * FROM {table_name}")
#         rows = cursor.fetchall()  # Get all rows
#     return columns, rows
#
#
# # Add Record - Show form to add a new record to the table
# def add_record(request, table_name):
#     if request.method == 'POST':
#         data = {col: request.POST.get(col) for col in get_table_columns(table_name)}
#         sql_operations.insert_record(table_name, data)
#         return redirect('table_view', table_name=table_name)
#     return render(request, 'add_record.html', {'table_name': table_name, 'columns': get_table_columns(table_name)})
#
#
# # Function to get columns of a table
# def get_table_columns(table_name):
#     with connection.cursor() as cursor:
#         cursor.execute(f"DESCRIBE {table_name}")
#         columns = [row[0] for row in cursor.fetchall()]
#     return columns
#
#
# # Edit Record - Show form to edit an existing record
# def edit_record(request, table_name, pk):
#     columns, _ = get_table_data(table_name)
#     if request.method == 'POST':
#         data = {col: request.POST.get(col) for col in columns}
#         sql_operations.update_record(table_name, pk, data)
#         return redirect('table_view', table_name=table_name)
#
#     record = get_record(table_name, pk)
#     return render(request, 'edit_record.html', {'table_name': table_name, 'columns': columns, 'record': record})
#
#
# # Function to get a specific record
# def get_record(table_name, pk):
#     with connection.cursor() as cursor:
#         cursor.execute(f"SELECT * FROM {table_name} WHERE id = %s", [pk])
#         return cursor.fetchone()
#
#
# # Delete Record - Show confirmation page before deletion
# def confirm_delete(request, table_name, pk):
#     columns, rows = get_table_data(table_name)
#     record = get_record(table_name, pk)
#     if request.method == 'POST':
#         sql_operations.delete_record(table_name, pk)
#         return redirect('table_view', table_name=table_name)
#     return render(request, 'confirm_delete.html', {'columns': columns, 'record': record, 'table_name': table_name})
from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
import MySQLdb

import MySQLdb
from django.shortcuts import render


def home(request):
    try:
        # Establish a connection to the remote MySQL server
        db = MySQLdb.connect(
            user='u919924273_admin',
            password='Spacio0310',
            host='185.28.21.52',  # Remote MySQL server host
            database='u919924273_workspace'  # Database name
        )
        cursor = db.cursor()

        # Execute SQL to show all tables in the database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()  # Fetch all table names

        cursor.close()  # Close the cursor

        # Return the list of tables to the template
        return render(request, 'mycrudapp/home.html', {'tables': tables})

    except MySQLdb.OperationalError as e:
        # Handle any connection errors
        print(f"Error: {e}")
        return render(request, 'mycrudapp/error.html', {'error': str(e)})


def table_view(request, table_name):
    # Query all rows from the selected table
    db = MySQLdb.connect(user='your_mysql_username', password='your_mysql_password', host='localhost', database='your_database_name')
    cursor = db.cursor()
    cursor.execute(f"DESCRIBE {table_name}")
    columns = [column[0] for column in cursor.fetchall()]
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    cursor.close()
    return render(request, 'mycrudapp/table_view.html', {'table_name': table_name, 'columns': columns, 'rows': rows})

def add_record(request, table_name):
    if request.method == 'POST':
        # Logic for adding a new record to the table
        pass
    return render(request, 'mycrudapp/add_record.html', {'table_name': table_name})

def edit_record(request, table_name, pk):
    if request.method == 'POST':
        # Logic for editing the record
        pass
    return render(request, 'mycrudapp/edit_record.html', {'table_name': table_name, 'pk': pk})

def confirm_delete(request, table_name, pk):
    if request.method == 'POST':
        # Logic for deleting the record
        pass
    return render(request, 'mycrudapp/confirm_delete.html', {'table_name': table_name, 'pk': pk})
