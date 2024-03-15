import json
import sqlite3


# creating json object from database query 


connection_string = 'Driver={SQL Server};Server=my_server;Database=my_database;UID=my_username;PWD=my_password;'

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

sql_query = "SELECT * from table;"

cursor.execute(sql_query)

columns = [column[0] for column in cursor.description]

data = [dict(zip(columns, row)) for row in cursor.fetchall()]

json_data = json.dumps(data, indent=4)

print(json_data) 