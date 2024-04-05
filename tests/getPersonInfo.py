import json
import requests


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwOTk3MTgwZTNkOGQ3MGRjNzMzY2QyOTc4MzQwZmJkYyIsInN1YiI6IjY1ZWYyNjYxZWZlMzdjMDE2M2VlMjczNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.o--9MNz6CXWLp4Q_WnIZOZrbAOEtD1KwyolxwHHZeK4"
}

i = 1
while True:
    print("https://api.themoviedb.org/3/person/" + str(i))
    url = "https://api.themoviedb.org/3/person/" + str(i)
    response = requests.get(url, headers=headers)
    personJSON = response.json()

    if "success" not in personJSON:
        url = "https://api.themoviedb.org/3/person/" + str(i) + "/movie_credits"
        response = requests.get(url, headers=headers)
        mCreditsJSON = response.json()
        f = open("personInfo.txt","w")
        f.write(json.dumps(personJSON, indent=4))
        f.write(json.dumps(mCreditsJSON, indent=4))
        f.close
        break

    else:
        i+=1
