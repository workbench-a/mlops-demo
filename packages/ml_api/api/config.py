"""ML API configuration.
"""
import pathlib
import os
from dotenv import load_dotenv

# Set the package root to the parent of the parent of the currrent directory
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

# Set the environment path to ./.env
env_path = PACKAGE_ROOT / '.env'
load_dotenv(dotenv_path=env_path)

# Database uri
DATABASE_ENGINE = os.environ.get('DATABASE_ENGINE')
DATABASE_PATH = pathlib.Path(__file__).resolve() / 'api' / \
    'data' / 'databases' / os.environ.get('DATABASE_PATH')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_ADDRESS = os.environ.get('DATABASE_ADDRESS')

# Twitter Credentials
## Consumer keys
TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
TWITTER_API_KEY_SECRET = os.environ.get('TWITTER_API_KEY_SECRET')
# Twitter authentication tokens
## Access token and secret
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
## Data Access

# For developing models locally
MODEL_DEVELOPMENT = True
MODEL_PATHS = [os.environ.get('DEMO_MODEL_PATH')]

# Flask app config

class Config:
    """Base configuration class, specifying SERVER_PORT,
    DEBUG, and TESTING configurations
    """
    DEBUG = False
    TESTING = False
    SERVER_PORT = 5000

class DevelopmentConfig(Config):
    """Flask development configuration.
    """
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Flask Production configuration. and database uri.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    DEBUG = False
    SERVER_ADDRESS: os.environ.get('SERVER_ADDRESS', '0.0.0.0')
    SERVER_PORT: os.environ.get('SERVER_PORT', '5000')
