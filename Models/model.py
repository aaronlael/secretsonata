from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(32))

    def __init__(self, email, name):
        self.id
        self.email = email
        self.name = name
    
    def __repr__(self):
        return f"<Name: {self.name}>"


class ExchangeGroup(db.Model):
    __tablename__ = 'ExchangeGroup'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    creatorId = db.Column(db.Integer())

    def __init__(self, name, creatorid):
        self.id
        self.name = name
        self.creatorId = creatorid

    def __repr__(self):
        return f"<Name: {self.name}>"

           
class UserGroups(db.Model):
    __tablename__ = 'UserGroups'

    id = db.Column(db.Integer, primary_key=True)
    groupId = db.Column(db.Integer())
    santaUserId = db.Column(db.Integer())
    receiverUserId = db.Column(db.Integer())
    playlistUrl = db.Column(db.String())

    def __init__(self, groupId, santaUserId, receiverUserId):
        self.id
        self.groupId = groupId
        self.santaUserId = santaUserId
        self.receiverUserId = receiverUserId
        self.playlistUrl
    
        def setplaylist(self, playlist):
            self.playlistUrl = playlist


    def __repr__(self):
        return f"<Playlist: {self.playlistUrl}>"

class Songs(db.Model):
    __tablename__ = 'Songs'

    id = db.Column(db.Integer, primary_key=True)
    songName = db.Column(db.String())
    artist = db.Column(db.String())
    link = db.Column(db.String())


    def __init__(self, songname, artist, link):
        self.id
        self.songName = songname
        self.artist = artist
        self.link = link

    def __repr__(self):
        return f"<Song: {self.songName} - {self.artist}>"


class Preferences(db.Model):
    __tablename__ = 'Preferences'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer())
    songIds = db.Column(db.String())


    def __init__(self, userid, songids):
        self.id
        self.userId = userid
        self.songIds = songids

    def __repr__(self):
        songs = ", ".join(self.songIds.split("|"))
        return f"<UserId: {self.userId}, SongIds: {songs}>"
    


