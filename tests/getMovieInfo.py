import json
import requests

movieID = 0
movieDetailURL = "https://api.themoviedb.org/3/movie/" + movieID
movieCastURL = "https://api.themoviedb.org/3/movie/" + movieID + "/credits"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOTk3MTgwZTNkOGQ3MGRjNzMzY2QyOTc4MzQwZmJkYyIsInN1YiI6IjY1ZWYyNjYxZWZlMzdjMDE2M2VlMjczNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.o--9MNz6CXWLp4Q_WnIZOZrbAOEtD1KwyolxwHHZeK4"
}

i = 1
while True:
    print("https://api.themoviedb.org/3/movie/" + str(i) + "?language=en-US")
    url = "https://api.themoviedb.org/3/movie/" + str(i) + "?language=en-US"
    response = requests.get(url, headers=headers)
    movieJSON = response.json()

    if "success" not in movieJSON:
        url = "https://api.themoviedb.org/3/movie/" + str(i) + "/credits"
        response = requests.get(url, headers=headers)
        castJSON = response.json()
        f = open("movieInfo.txt","x")
        f.write(json.dumps(movieJSON, indent=4))
        f.write(json.dumps(castJSON, indent=4))
        f.close
        break

    else:
        i+=1




