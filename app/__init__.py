from flask import Flask
from config import Config
from db.helpers import get_db

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Ensure the instance folder exists
    import os
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Import and register blueprints
    # Import and register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.booking import booking_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.admin import admin_bp
    from app.routes.certificate import certificate_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(certificate_bp)

    return app
