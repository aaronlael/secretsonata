from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import os
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def servesite():
    pass


class MetaLines(db.Model):
    __tablename__ = 'metalines'

    id = db.Column(db.Integer, primary_key=True)
    line = db.Column(db.String())
    count = db.Column(db.Integer())

    def __init__(self, line):
        self.id
        self.line = line
        self.count = 0

    def __repr__(self):
        return f"<Line: {self.line}>"


if __name__ == "__main__":
    app.run()
