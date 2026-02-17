# config.py
import os
from datetime import timedelta

# Use environment variable for production - these will need to be set before use
SECRET_KEY = os.environ.get('SECRET_KEY')
SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT")

DEBUG = True



#allow registration
SECURITY_REGISTERABLE = True

#temporarily remove email on registration to simplify for this exercise
SECURITY_SEND_REGISTER_EMAIL = False

#changed from default of argon2 for the purposes of this exercise to simplify
SECURITY_PASSWORD_HASH = 'bcrypt'

#SECURITY_PASSWORD_COMPLEXITY_CHECKER = 'zxcvbn'

# initialise sessions
REMEMBER_COOKIE_SAMESITE = "strict"
SESSION_COOKIE_SAMESITE = "strict"
SESSION_PERMANENT = True  # Sessions are permanent unless specified by event or configuration
SESSION_TYPE = "filesystem"  # Store session data in files
SESSION_COOKIE_HTTPONLY = True  # Sessions not accessible from JavaScript
SESSION_COOKIE_SECURE = True  # Sessions require an encrypted connection

# set the session maximum duration
# TODO check the required duration and adjust from 30 minutes if required.
PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)

# Use an in-memory db and prevent timeouts
SQLALCHEMY_DATABASE_URI = 'sqlite://'
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
}
SQLALCHEMY_TRACK_MODIFICATIONS = False