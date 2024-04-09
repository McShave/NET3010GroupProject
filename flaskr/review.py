import sqlite3
import json
import sys

from flaskr.db import get_db



def addMovieReview(movieReview, movieScore, movieID, userID):
    # add a movie review to user_move_review table in database
    # use g.user to find username, then query user table to retrieve userID
    # user movieID as movieID

    movieScore = returnScoreInt(movieScore)

    f = open("movieReviewTest.txt", "w")
    f.write(f"movieReview ({type(movieReview)}): {movieReview}\n")
    f.write(f"movieScore ({type(movieScore)}): {movieScore}\n")
    f.write(f"movieID ({type(movieID)}): {movieID}\n")
    f.write(f"userID ({type(userID)}): {userID}\n")

    db = get_db()

    data = db.execute("SELECT reviewID, userID, movieID, review, score from user_movie_review WHERE userID=? and movieID=?", (userID, movieID)).fetchone()
    
    if data:
        reviewID = data[0]
        score = data[4]
        review = data[3]
        if not movieReview.strip():
            db.execute("REPLACE INTO user_movie_review (reviewID, movieID, userID, review, score) values (?, ?, ?, ?, ?)", 
                (reviewID, movieID, userID, review, movieScore)) 

        elif not movieScore:
            db.execute("REPLACE INTO user_movie_review (reviewID, movieID, userID, review, score) values (?, ?, ?, ?, ?)", 
                (reviewID, movieID, userID, movieReview, score))
        else:
            db.execute("Replace INTO user_movie_review (reviewID, movieID, userID, score, review) values (?, ?, ?, ?, ?)", 
                (reviewID, movieID, userID, movieScore, movieReview))

        db.commit()
        return
        
    else:
        if not movieReview.strip():
            db.execute("INSERT INTO user_movie_review (movieID, userID, score) values (?, ?, ?)", 
                   (movieID, userID, movieScore))
        elif not movieScore:
            db.execute("INSERT INTO user_movie_review (movieID, userID, review) values (?, ?, ?)", 
                   (movieID, userID, movieReview))
        else:
            db.execute("INSERT INTO user_movie_review (movieID, userID, score, review) values (?, ?, ?, ?)", 
                    (movieID, userID, movieScore, movieReview))
        db.commit()
        return

def returnScoreInt(movieScore):
    
    if movieScore == "one":
        return 1
    if movieScore == "two":
        return 2
    if movieScore == "three":
        return 3
    if movieScore == "four":
        return 4
    if movieScore == "five":
        return 5
    if movieScore == "six":
        return 6
    if movieScore == "seven":
        return 7
    if movieScore == "eight":
        return 8
    if movieScore == "nine":
        return 9
    if movieScore == "ten":
        return 10
    else:
        return None

def addToWatchlist(movieID):
    # add an data row to user_watch_next table in database
    # use g.user to find username, then query user table to retrieve userID
    # user movieID as movieID entry

    return