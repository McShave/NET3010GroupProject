#requires "python3 -m pip install request" for windows
#or "sudo apt-get install python3-requests"

import requests
import json

url = "https://api.themoviedb.org/3/movie/300?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOTk3MTgwZTNkOGQ3MGRjNzMzY2QyOTc4MzQwZmJkYyIsInN1YiI6IjY1ZWYyNjYxZWZlMzdjMDE2M2VlMjczNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.o--9MNz6CXWLp4Q_WnIZOZrbAOEtD1KwyolxwHHZeK4"
}

response = requests.get(url, headers=headers)

respJSON = response.json()

respStr = json.dumps(respJSON, indent=4)

f = open("tmdbapicall.txt", "w")

f.write(respStr)

f.close()

f = open("tmdbapicall.txt", "r")

print(f.read())

f.close()