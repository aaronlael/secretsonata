from Models.model import User
from flask.blueprints import Blueprint
from flask import render_template, request

logon = Blueprint('logon', __name__,
                template_folder='templates',
                static_folder='static')

@logon.route('/')
def logonpage():
    user = User.query.filter_by(email="aaron.j.lael@gmail.com").first()
    return f"user ID for {user.name} is {user.id}"