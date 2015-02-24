from flask import Flask
from flask.ext.babel import Babel


babel = Babel()

def create_app():
    ''' Create the Flask app.
    '''
    # Create the Flask app.
    app = Flask(__name__)

    register_url_rules(app)

    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        print 'GET_LOCALE'
        return 'en'

    return app


# Views for Page rendering
from views.index import Index


def register_url_rules(app):
    ''' Register URLs
    :param app: The Flask application instance.
    '''
    # Register the URL rules for JSON requests.
    register_json_url_rules(app)

    # Register the URL rules for page requests.
    register_page_url_rules(app)


def register_json_url_rules(app):
    pass;


def register_page_url_rules(app):
    ''' Register the URL rules for page requests.
    :param app: The Flask application instance.
    '''
    # Index.
    app.add_url_rule(
        '/',
        view_func=Index.as_view('index'))