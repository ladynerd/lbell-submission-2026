import os

from flask import Flask, render_template
from datetime import timedelta

import bcrypt

from flask_sqlalchemy import SQLAlchemy

from flask_security import Security, SQLAlchemyUserDatastore, auth_required, hash_password
from flask_security.models import fsqla_v3 as fsqla

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman

# Create app
app = Flask(__name__)

# Load configuration from the config.py file
app.config.from_object('config')



# Apply basic rate limiting to prevent enumeration and bruteforce attacks
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["20 per minute", "1 per second"],
    storage_uri="memory://",
    strategy="fixed-window",
)

# TODO Requires HTTPS to be working first - see submission.md for details
# provides CORS, CSP and Security Controls https://github.com/wntrblm/flask-talisman
#Talisman(app)

# add CSRF protections https://pypi.org/project/Flask-SeaSurf/
# csrf = SeaSurf(app)

# SELF = "'self'"

# Configurate Talisman for basic content security policy
# talisman = Talisman(
#     app,
#     content_security_policy={
#         'default-src': SELF,
#         # allow images from all locations
#         'img-src': '*',
#         # allow scripts from a specific CDN
#         'script-src': [
#             SELF,
#             'some.cdn.com',
#         ],
#         # allow CSS and styles from a specific CDN
#         'style-src': [
#             SELF,
#             'another.cdn.com',
#         ],
#     },
#     content_security_policy_nonce_in=['script-src'],
#     feature_policy={
#         'geolocation': '\'none\'',
#     },
#     permissions_policy={
#         'geolocation': '()',
#     }
# )

# Create database connection object
db = SQLAlchemy(app)

# Define models
fsqla.FsModels.set_db_info(db)

class Role(db.Model, fsqla.FsRoleMixin):
    pass

class User(db.Model, fsqla.FsUserMixin):
    pass

# Create database objects
with app.app_context():
    db.create_all()

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Views
@app.route("/")
@auth_required()
def home():
    return render_template("home.html", message="Hello World")



if __name__ == '__main__':
    app.run(debug=True)

    # local workaround for ssl - this won't work as it requires a full certificate
    #app.run(debug=True, ssl_context="adhoc")