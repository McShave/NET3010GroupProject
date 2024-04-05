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

    returnJSON = {}

    return returnJSON

def queryPerson(personSearch):
    #takes a string personSearch and retrieves person seach from tmdb.com
    #returns a json object in the form of:
    #{ "people" : [{"name" : "", "year_of_birth" : "", "pathtopicture" : "", "personID" : ""},
    #              {"name" : "", "year_of_birth" : "", "pathtopicture" : "", "personID" : ""},
    #              etc ]}

    returnJSON = {}

    return returnJSON

def getMovieInfo(movieJSON):
    #takes an interger movieID and retrieves that movie's information from tmdb.com
    #this will require 2 api calls, one for movie details, one for cast/crew

    #returns a json object in the form of:

    #{"details" : {"name" : "", "tagline" : "", "runtime": "", "releaseDate" : "",
    #              "summary" : "", "language": "", "pathtoposter" : "", "movieID" : "",           
    # "cast" : [{"name" : "", "character" : "", "personID" : ""}],
    # "crew": [{"name": "", "role", "personID" : ""}] }

    returnJSON = {}

    return returnJSON

def getPersonInfo(personJSON):
    #takes an interger movieID and retrieves that movie's information from tmdb.com
    #returns a json object in the form of:
    #{"name" : "", "birthday" : "", "pathtopicture" : "", "personID" : "",
    # "roles" : [] }

    returnJSON = {}

    return returnJSON