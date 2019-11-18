# Web Application made with Flask

# ==================== #
#     Requirements     #
# ==================== #

# Import Flask and its requirements
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Import Configuration
from app.config import Config


# Initiating Elements
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
marsh = Marshmallow()

# Login manager configuration
# login_manager.login_view = 'auth.login'
# login_manager.login_message = None

# Database migration for Web Application
migrate = Migrate()


def create_app(config_class = Config):
    # Init app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init Elements
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    marsh.init_app(app)

    # Init Database Management
    migrate.init_app(app, db)

    # Import a module/component using its blueprint handler variable
    from app.mod_main.controllers import main_module
    from app.mod_error.handlers import error_module
    # insert here....

    # Register the route blueprints
    app.register_blueprint(main_module)
    app.register_blueprint(error_module)
    # insert here....

    return app

# Database manager for Web Application
manager = Manager(create_app())
manager.add_command('db', MigrateCommand)



    