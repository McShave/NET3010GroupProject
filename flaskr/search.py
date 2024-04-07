import sqlite3
import json

import requests
import os


# f = open("searchresults.txt", "x")
# f.write(json.dumps(respjson, indent=4))
# f.close()
# print(json.dumps(respjson, indent=4))

# f = open(os.path.relpath("searchresults.txt"), "r")
# flines = f.readlines()
# ftext = ""
# for line in flines:
#     ftext += line
# jobj = json.loads(ftext)

# for movie in jobj["results"]:
#     print(movie["original_title"])

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTFmZDBkYWQ5YThiOTQ3MDIyZjk1OWMyYjYzYzVlOCIsInN1YiI6IjY2MDA3OTNjMWIxZjNjMDE2Mzk4NmRlZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xTKi7Ih88L9PfBeQU0GbMLhahGX0lTOnyjMqbc32O3o"
}

movieID = 0
movieDetailURL = "https://api.themoviedb.org/3/movie/" + str(movieID)
movieCastURL = "https://api.themoviedb.org/3/movie/" + str(movieID) + "/credits"

personID = 0
personDetailURL = "https://api.themoviedb.org/3/person/" + str(personID)
personMovieCreditsURL = "https://api.themoviedb.org/3/person/" + str(personID) + "/movie_credits"

# response = requests.get(url, headers=headers)
# respjson = json.loads(response.text)


def queryMovie(movieSearch):
    #takes string movieSearch retrieves movie search from tmdb.com
    #returns a json object in the form of:
    #{ "movies" : [{"title" : "", "year" : "", "pathtoposter" : "", "movieID" : ""},
    #              {"title": "", "year" : "", "pathtoposter" : "", "movieid" : ""},
    #               etc ]}

    response = requests.get("https://api.themoviedb.org/3/search/movie", params={"query": movieSearch}, headers=headers)
    respjson = response.json()

    movies = []
    for movie in respjson["results"]:
        movie_info = {
            "title": movie["original_title"],
            "year": movie["release_date"].split("-")[0] if movie["release_date"] else "",
            "pathtoposter": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie['poster_path'] else "",
            "movieID": str(movie["id"])
        }
        movies.append(movie_info)

    returnJSON = {"movies": movies}

    with open("searchresultMovie.txt", "w") as f:
        json.dump(returnJSON, f, indent=4)
        
    return returnJSON

# TESTING
movie_search_query = "Pet Sematary"
movie_search_results = queryMovie(movie_search_query)
print(json.dumps(movie_search_results, indent=4))

with open("searchresultMovie.txt", "r") as file:
    data = file.read()

print(data)


def queryPerson(personSearch):
    #takes a string personSearch and retrieves person search from tmdb.com
    #returns a json object in the form of:
    #{ "people" : [{"name" : "", "year_of_birth" : "", "pathtopicture" : "", "personID" : ""},
    #              {"name" : "", "year_of_birth" : "", "pathtopicture" : "", "personID" : ""},
    #              etc ]}
    response = requests.get("https://api.themoviedb.org/3/search/person?include_adult=false&language=en-US&page=1", params={"query": personSearch}, headers=headers)
    respjson = response.json()

    people = []
    for person_data in respjson["results"]:
        person_info = {
            "name": person_data["name"],
            "year_of_birth": person_data["birthday"] if "birthday" in person_data else "Unknown",
            "pathtopicture": f"https://image.tmdb.org/t/p/w500{person_data['profile_path']}" if person_data['profile_path'] else "",
            "personID": str(person_data["id"])
        }
        people.append(person_info)

    returnJSON = {"people": people}

    # Write JSON data to file
    with open("searchresultPerson.txt", "w") as f:
        json.dump(returnJSON, f, indent=4)
        
    return returnJSON

# TESTING
person_search_query = "Keanu Reeves"
person_search_results = queryPerson(person_search_query)
print(json.dumps(person_search_results, indent=4))

with open("searchresultPerson.txt", "r") as file:
    data = file.read()

print(data)


def getMovieInfo(movieID):
    #takes an integer movieID and retrieves that movie's information from tmdb.com
    #this will require 2 api calls, one for movie details, one for cast/crew

    #returns a json object in the form of:

    #{"details" : {"name" : "", "tagline" : "", "runtime": "", "releaseDate" : "",
    #              "summary" : "", "language": "", "pathtoposter" : "", "movieID" : "",           
    # "cast" : [{"name" : "", "character" : "", "personID" : ""}],
    # "crew": [{"name": "", "role", "personID" : ""}] }
    response_details = requests.get(f"https://api.themoviedb.org/3/movie/{movieID}", headers=headers)
    movie_details = response_details.json()

    details_info = {
        "name": movie_details.get("original_title", ""),
        "tagline": movie_details.get("tagline", ""),
        "runtime": movie_details.get("runtime", ""),
        "releaseDate": movie_details.get("release_date", "").split("-")[0] if movie_details.get("release_date") else "",
        "summary": movie_details.get("overview", ""),
        "language": movie_details.get("original_language", ""),
        "pathtoposter": f"https://image.tmdb.org/t/p/w500{movie_details['poster_path']}" if movie_details.get('poster_path') else "",
        "movieID": str(movieID),
    }

    response_credits = requests.get(f"https://api.themoviedb.org/3/movie/{movieID}/credits", headers=headers)
    credits = response_credits.json()

    cast = []
    for actor in credits["cast"]:
        cast.append({
            "name": actor["name"],
            "character": actor["character"],
            "personID": str(actor["id"])
        })

    crew = []
    for member in credits["crew"]:
        crew.append({
            "name": member["name"],
            "role": member["job"],
            "personID": str(member["id"])
        })

    returnJSON = {
        "details": details_info,
        "cast": cast,
        "crew": crew
    }

    with open("searchresultMovieID.txt", "w") as f:
        json.dump(returnJSON, f, indent=4)
        
    return returnJSON

# TESTING
movie_search_query = 8913
movie_search_results = getMovieInfo(movie_search_query)
print(json.dumps(movie_search_results, indent=4))

with open("searchresultMovieID.txt", "r") as file:
    data = file.read()

print(data)

def getPersonInfo(personID):
    #takes an integer movieID and retrieves that movie's information from tmdb.com
    #returns a json object in the form of:
    #{"name" : "", "birthday" : "", "pathtopicture" : "", "personID" : "",
    # "roles" : [] }

    response_person = requests.get(f"https://api.themoviedb.org/3/person/{personID}", headers=headers)
    person_details = response_person.json()

    returnJSON = {
        "name": person_details.get("name", ""),
        "birthday": person_details.get("birthday", ""),
        "pathtopicture": f"https://image.tmdb.org/t/p/w500{person_details['profile_path']}" if person_details.get('profile_path') else "",
        "personID": str(personID),
        "roles": []
    }

    response_credits = requests.get(f"https://api.themoviedb.org/3/person/{personID}/movie_credits", headers=headers)
    credits = response_credits.json()

    for role in credits.get("cast", []):
        returnJSON["roles"].append({
            "movieID": str(role["id"]),
            "character": role["character"],
            "title": role["title"]
        })

    return returnJSON

# TESTING
person_search_query = 6384
person_search_results = getPersonInfo(person_search_query)
print(json.dumps(person_search_results, indent=4))