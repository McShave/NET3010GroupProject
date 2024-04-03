import requests
import json

url = "https://api.themoviedb.org/3/search/movie?query=batman&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOTk3MTgwZTNkOGQ3MGRjNzMzY2QyOTc4MzQwZmJkYyIsInN1YiI6IjY1ZWYyNjYxZWZlMzdjMDE2M2VlMjczNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.o--9MNz6CXWLp4Q_WnIZOZrbAOEtD1KwyolxwHHZeK4"
}

response = requests.get(url, headers=headers)

respJ = json.loads(response.text)
print(json.dumps(respJ, indent=4))