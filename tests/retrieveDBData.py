import json
import sqlite3
import os


# creating json object from database query 

conn = sqlite3.connect(os.path.relpath("instance\\flaskr.sqlite"))

cursor = conn.cursor()

sql_query = "SELECT username FROM user;"

conn.execute(sql_query)

tables = cursor.fetchall()

print(tables)
# columns = [column[0] for column in cursor.description]

# data = [dict(zip(columns, row)) for row in cursor.fetchall()]

# json_data = json.dumps(data, indent=4)

# print(json_data) 