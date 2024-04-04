import sqlite3
import json

import click
from flask import current_app, g

import requests
import os

# url = "https://api.themoviedb.org/3/search/movie?query=batman%20joker&include_adult=false&language=en-US&page=1"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTFmZDBkYWQ5YThiOTQ3MDIyZjk1OWMyYjYzYzVlOCIsInN1YiI6IjY2MDA3OTNjMWIxZjNjMDE2Mzk4NmRlZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xTKi7Ih88L9PfBeQU0GbMLhahGX0lTOnyjMqbc32O3o"
# }

# response = requests.get(url, headers=headers)

# respjson = json.loads(response.text)

# f = open("searchresults.txt", "x")
# f.write(json.dumps(respjson, indent=4))
# f.close()
# print(json.dumps(respjson, indent=4))

f = open(os.path.relpath("searchresults.txt"), "r")
flines = f.readlines()
ftext = ""
for line in flines:
    ftext += line
jobj = json.loads(ftext)

for movie in jobj["results"]:
    print(movie["original_title"])