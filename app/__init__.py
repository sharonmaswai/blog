from config import config_options
from flask import Flask

def create_app(config_name):

     # Creating the app configurations    
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app