import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'green-exp-dev-secret-2025')
    INSTANCE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
    DATABASE = os.path.join(INSTANCE_PATH, 'green_experience.db')

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True


CONFIG_MAP = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
