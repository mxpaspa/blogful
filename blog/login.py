from flask.ext.login import LoginManager
from flask import flash
from flask.ext.login import login_user
from werkzeug.security import check_password_hash
from .database import User
from . import app
from .database import session, User

login_manager = LoginManager() #instance
login_manager.init_app(app)

login_manager.login_view = "login_get" #where does login.view come from?
login_manager.login_message_category = "danger"

@login_manager.user_loader
def load_user(id):
    return session.query(User).get(int(id))

