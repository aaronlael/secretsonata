from flask import Flask
from Models.model import db, User
from views import logon
import os


def create_app():
    app = Flask(__name__)
    app.register_blueprint(logon)
    app.config['DEBUG'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']
    db.init_app(app)
    return app

def setup_db(app):
    with app.app_context():
        db.create_all()
    user = User("aaron.j.lael@gmail.com", "Aaron Lael")
    if User.query.filter(User.email == user.email).first():
        # user already exists
        pass
    else:
        db.session.add(user)
        db.session.commit()


if __name__ == "__main__":
    app = create_app()
    app.app_context().push()
    setup_db(app)
    app.run()