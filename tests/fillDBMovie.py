import json
import sqlite3
import os
import requests
import functools




db = sqlite3.connect(os.path.abspath("C:\\Users\\Mitch Schaefer\\Flashback\\instance\\flaskr.sqlite"))
c = db.cursor()

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOTk3MTgwZTNkOGQ3MGRjNzMzY2QyOTc4MzQwZmJkYyIsInN1YiI6IjY1ZWYyNjYxZWZlMzdjMDE2M2VlMjczNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.o--9MNz6CXWLp4Q_WnIZOZrbAOEtD1KwyolxwHHZeK4"
}

x = range(93306, 1000000)

for num in x:
    print("https://api.themoviedb.org/3/movie/" + str(num) + "?language=en-US")
    url = "https://api.themoviedb.org/3/movie/" + str(num) + "?language=en-US"
    response = requests.get(url, headers=headers)
    respJSON = response.json()
    if {"id", "title", "release_date"} <= respJSON.keys():
        print("#"+str(num)+" success")
        # print(str(respJSON["id"])+": "+respJSON["title"]+", "+str(respJSON["release_date"][:4]))
        try:
            c.execute("INSERT INTO movie VALUES(?, ?, ?, ?)", (int(respJSON["id"]), str(respJSON["title"]), 0, int(respJSON["release_date"][:4])))
            db.commit()
        except:
            print("error has occurred")

