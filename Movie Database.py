import sqlite3

conn = sqlite3.connect("C:\\Users\\halim\\MovieDB.db")
cur = conn.cursor()

# Connect to a new database
cur.execute('''CREATE TABLE IF NOT EXISTS Movie (MovieID INTEGER PRIMARY KEY, Name TEXT, Rating NUMERIC, "Release Year" INTEGER)''')

cur.execute('''CREATE TABLE IF NOT EXISTS User (UserID INTEGER PRIMARY KEY, Username TEXT, Email TEXT, Password TEXT, ProfilePicture TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Person (PersonID INTEGER PRIMARY KEY, Name TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Genre (GenreID INTEGER PRIMARY KEY, Name TEXT)''') 

cur.execute('''CREATE TABLE IF NOT EXISTS User_Movie_Review (ReviewID INTEGER PRIMARY KEY, MovieID INTEGER, UserID INTEGER, Score INTEGER, Review TEXT, FOREIGN KEY(MovieID) REFERENCES Movie(MovieID), FOREIGN KEY(UserID) REFERENCES User(UserID))''')

cur.execute('''CREATE TABLE IF NOT EXISTS User_Watch_Next (WatchNextID INTEGER PRIMARY KEY, UserID INTEGER, MovieID INTEGER, FOREIGN KEY(UserID) REFERENCES User(UserID), FOREIGN KEY(MovieID) REFERENCES Movie(MovieID))''')
conn.commit()

cur.close()
conn.close()
