import sqlite3
import json

# User create
def create_user(conn, username, email, password, profile_picture):
    cur = conn.cursor()
    cur.execute('''INSERT INTO User (Username, Email, Password, ProfilePicture) VALUES (?, ?, ?, ?)''', (username, email, password, profile_picture))
    conn.commit()

# User edit
def edit_user(conn, user_id, new_username, new_email, new_password, new_profile_picture):
    cur = conn.cursor()
    cur.execute('''UPDATE User SET Username=?, Email=?, Password=?, ProfilePicture=? WHERE UserID=?''', (new_username, new_email, new_password, new_profile_picture, user_id))
    conn.commit()

# User delete
def delete_user(conn, user_id):
    cur = conn.cursor()
    cur.execute('''DELETE FROM User WHERE UserID=?''', (user_id,))
    conn.commit()

conn = sqlite3.connect("C:\\Users\\halim\\MovieDB.db")
cur = conn.cursor()

# Creating tables
cur.execute('''CREATE TABLE IF NOT EXISTS Movie (MovieID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT UNIQUE, Rating NUMERIC, "Release Year" INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS User (UserID INTEGER PRIMARY KEY AUTOINCREMENT, Username TEXT UNIQUE, Email TEXT UNIQUE, Password TEXT, ProfilePicture TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Person (PersonID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Genre (GenreID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS User_Movie_Review (ReviewID INTEGER PRIMARY KEY AUTOINCREMENT, MovieID INTEGER, UserID INTEGER, Score INTEGER, Review TEXT, FOREIGN KEY(MovieID) REFERENCES Movie(MovieID), FOREIGN KEY(UserID) REFERENCES User(UserID))''')
cur.execute('''CREATE TABLE IF NOT EXISTS User_Watch_Next (WatchNextID INTEGER PRIMARY KEY AUTOINCREMENT, UserID INTEGER, MovieID INTEGER, FOREIGN KEY(UserID) REFERENCES User(UserID), FOREIGN KEY(MovieID) REFERENCES Movie(MovieID))''')


def insertMoviesDB(movieDBa):
    conn = sqlite3.connect("movieDB.db")
    cur = conn.cursor()
    for movie in movieDBa:
        cur.execute('''INSERT INTO Movie (Name, Rating, ReleaseYear) VALUES (?, ?, ?)''', (movie["title"], movie["vote_average"], movie["release_date"][:4]))
    conn.commit()
    conn.close()

# Read data from file
with open("tmdbapicall.txt", "r") as file:
    api_response = json.load(file)

# Extract data from API response
movieDB = api_response["results"]

# Insert data into database
insertMoviesDB(movieDB)

print("Data inserted into database.")


conn.commit()

cur.close()
conn.close()