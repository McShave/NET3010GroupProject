import os

from flask import (Flask, render_template, request, redirect, url_for, session)


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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
<<<<<<< HEAD
    @app.route('//', methods=['GET', 'POST'])
=======
    @app.route('//')
>>>>>>> b053eb248f70b8774eae17837c5368973893e4b0
    def index():
        if request.method == 'GET':
            moviesearch = request.form["moviesearch"]
            session["message"] = moviesearch
            #do api search with moviesearch
            return redirect(url_for('advancedsearch'))
        return render_template('index.html')
    
    @app.route('/basic_search')
    def basic_search():
        return render_template('basic_search.html')
    
    @app.route('/advancedsearch')
    def advancedsearch():
        message = session["message"]
        return render_template('advancedsearch.html')

    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app