"""
Configuration file with settings and API keys from third-party services
"""
import os
from dotenv import load_dotenv

# Loading env variables from .env file
load_dotenv('.env')

ENVIRONMENT = os.environ.get('APP_NAME', 'dev')  # Available environments: dev / prod

# ↓ API variables ↓
APP_NAME = os.environ.get('APP_NAME', 'MyApp')
API_HOST = os.environ.get('API_HOST', 'localhost')
API_PORT = os.environ.get('API_PORT', 8000)

# AWS KEY
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# BUCKET NAME
BUCKET = os.environ.get("BUCKET")
