from django.db import connection

# Insert a new record into a table
def insert_record(table_name, data):
    with connection.cursor() as cursor:
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{v}'" for v in data.values()])
        cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")

# Update an existing record in a table
def update_record(table_name, pk, data):
    set_clause = ', '.join([f"{col} = '{val}'" for col, val in data.items()])
    with connection.cursor() as cursor:
        cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE id = %s", [pk])

# Delete a record from a table
def delete_record(table_name, pk):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", [pk])
