from flask import (Flask, render_template)
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static', static_folder='../statics')
db = SQLAlchemy(engine_options={"max_identifier_length": 128})
login_manager = LoginManager()


def create_app(config):
    """
    Create application instance
    """
    # Import models to create them and process further
    # Initialize Flask application
    app.config.from_object(config)
    config.init_app(app)

    from .auth.models import (user_loader, AnonymousUser, unauthorized)
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.init_app(app)
    login_manager.user_loader(user_loader)
    login_manager.anonymous_user = AnonymousUser
    login_manager.login_view = "auth.login"
    login_manager.unauthorized_handler = unauthorized

    # Append blueprints
    from .auth import auth_app
    from .landing import landing_app
    from .admin import admin_app

    admin_app.init_app(app)
    app.register_blueprint(auth_app)
    app.register_blueprint(landing_app)

    return app


@app.errorhandler(404)
def page_not_found(error):
    """Page not found (404) error handler"""

    return render_template('404.html')


@app.errorhandler(500)
def internal_server_error(error):
    """Internal server (500) error handler """

    return render_template('500.html')
