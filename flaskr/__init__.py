import os
import sys

from flask import (Flask, render_template, request, redirect, url_for, session, flash)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import search

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('//', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            session["search"] = request.form["moviesearch"]
            return redirect(url_for('movie_list'))
        return render_template('index.html')
    
    @app.route('/person_search', methods=('GET', 'POST'))
    def person_search():
        if request.method == 'POST':
            session["search"] = request.form["personsearch"]
            return redirect(url_for('person_list'))
        return render_template('person_search.html')
    
    @app.route('/movie_list')
    def movie_list():
        
        query = search.queryMovie(session["search"])
        #query = {"movies" : ["happy", "sad"]}
        return render_template('movie_list.html', query=query)
        # return render_template('movie_list.html', search=session["search"])
    
    @app.route('/person_list')
    def person_list():
        query = search.queryPerson(session["search"])
        return render_template('person_list.html', query=query)
        # return render_template('person_list.html', search=session["search"])
    
    @app.route('/movie_info/<id>')
    def movie_info(id):
        # print("rendering movie detail", file=sys.stderr)
        movieDetail = search.getMovieInfo(id)
        return render_template('movie_info.html', details=movieDetail)
    
    @app.route('/person_info/<id>')
    def person_info(id):
        personDetail = search.getPersonInfo(id)
        # personDetail = {}
        return render_template('person_info.html', details=personDetail)

    @app.route('/user_admin')
    def user_admin():
        return render_template('user_admin.html')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app