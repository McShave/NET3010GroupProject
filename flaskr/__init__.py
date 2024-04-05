import os

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
            return redirect(url_for('basic_search'))
        return render_template('index.html')
    
    @app.route('/basic_search')
    def basic_search():
        #query = search.queryMovie(session["search"])
        query = {"movies" : ["happy", "sad"]}
        return render_template('basic_search.html', query=query)
    
    @app.route('/advancedsearch')
    def advancedsearch():
        return render_template('advancedsearch.html')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app