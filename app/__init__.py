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
from views.hello import Hello


def register_url_rules(app):
    ''' Register URLs
    :param app: The Flask application instance.
    '''
    # Index.
    app.add_url_rule(
        '/',
        view_func=Index.as_view('index'))

    # Index.
    app.add_url_rule(
        '/hello',
        view_func=Hello.as_view('hello'))

    