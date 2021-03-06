from flask_sqlalchemy import SQLAlchemy
from six import integer_types
from sqlalchemy import Column, Integer, Float
from sqlalchemy.sql.sqltypes import DATE, STRINGTYPE, TEXT, DateTime, BOOLEAN
from sqlalchemy import Column, String, Integer

db = SQLAlchemy()

class users(db.Model):
  __tablename__ = 'users'
  id = db.Column(Integer, primary_key=True)
  username = db.Column(TEXT, unique=True)# emailカラム→usernameカラム
  hash = db.Column(TEXT, unique=False)
  nickname = db.Column(TEXT, unique=False)# nameカラム→nicknameカラム
  introduce = db.Column(TEXT, unique=False)# nameカラム→nicknameカラム
  
  def __init__(self, username=None, hash=None, nickname=None, introduce=None):
    self.username = username
    self.hash = hash
    self.nickname = nickname
    self.introduce = introduce


class song_locations(db.Model):
  __tablename__ = 'song_locations'
  id = db.Column(Integer, primary_key=True)
  user_id = db.Column(Integer, unique=False)
  track_id = db.Column(TEXT, unique=False)
  longitude = db.Column(Float, unique=False)
  latitude = db.Column(Float, unique=False)
  date = db.Column(DATE, unique=False)
  emotion = db.Column(TEXT, unique=False)
  comment = db.Column(TEXT, unique=False)
  is_private = db.Column(TEXT, unique=False)
  about = db.Column(TEXT, unique=False)

  def __init__(self, user_id=None, track_id=None, longitude=None, latitude=None, date=None, emotion = None, comment = None, is_private= None, about=None):
    self.user_id = user_id
    self.track_id = track_id
    self.longitude = longitude
    self.latitude = latitude
    self.date = date
    self.emotion = emotion
    self.comment = comment
    self.is_private = is_private
    self.about = about

class songs(db.Model):
  __tablename__ = 'songs'
  id = db.Column(Integer, primary_key=True)
  track_id = db.Column(TEXT, unique=True)
  track_name = db.Column(TEXT, unique=False)
  artist_name = db.Column(TEXT, unique=False)
  track_image = db.Column(TEXT, unique=False)
  spotify_url = db.Column(TEXT, unique=True)

  def __init__(self, track_id=None, track_name=None, artist_name=None, track_image=None, spotify_url=None):
    self.track_id = track_id
    self.track_name = track_name
    self.artist_name = artist_name
    self.track_image = track_image
    self.spotify_url = spotify_url

class follow(db.Model):
  __tablename__ = 'follow'
  id = db.Column(Integer, primary_key=True)
  follow_user_id = db.Column(Integer)
  followed_user_id = db.Column(Integer)

  def __init__(self, follow_user_id=None, followed_user_id = None):
    self.follow_user_id = follow_user_id
    self.followed_user_id = followed_user_id

class made_playlists(db.Model):
  __tablename__ = 'made_playlists'
  id = db.Column(Integer, primary_key=True)
  user_id = db.Column(Integer, unique=False)
  playlist_id = db.Column(TEXT, unique=False)
  playlist_uri = db.Column(TEXT, unique=False)
  playlist_image = db.Column(TEXT, unique=False)
  playlist_name = db.Column(TEXT, unique=False)


  def __init__(self, user_id=None, playlist_id=None, playlist_uri=None, playlist_image=None, playlist_name=None):
    self.user_id = user_id
    self.playlist_id = playlist_id
    self.playlist_uri = playlist_uri
    self.playlist_image = playlist_image
    self.playlist_name = playlist_name


class Group(db.Model):
  __tablename__ = 'Group'
  id = db.Column(Integer, primary_key=True)
  owner_id = db.Column(Integer)
  name = db.Column(TEXT, unique=False)
  introduction = db.Column(TEXT, unique=False)

  def __init__(self, owner_id=None, name=None, introduction=None):
    self.owner_id = owner_id
    self.name = name
    self.introduction = introduction
    
class UserGroup(db.Model):
  __tablename__ = 'UserGroup'
  id = db.Column(Integer, primary_key=True)
  group_id = db.Column(Integer)
  owner_id = db.Column(Integer)
  invited_id = db.Column(Integer)

  def __init__(self, group_id=None, owner_id = None, invited_id = None):
    self.group_id = group_id
    self.owner_id = owner_id
    self.invited_id = invited_id


class requests(db.Model):
  __tablename__ = 'requests'
  id = db.Column(Integer, primary_key=True)
  group_id = db.Column(Integer)
  owner_id = db.Column(Integer)
  invited_id = db.Column(Integer)

  def __init__(self, group_id=None, owner_id = None, invited_id = None):
    self.group_id = group_id
    self.owner_id = owner_id
    self.invited_id = invited_id

class likes(db.Model):
  __tablename__ = 'likes'
  id = db.Column(Integer, primary_key=True)
  user_id = db.Column(Integer)
  song_location_id = db.Column(Integer)
  datetime = db.Column(DateTime)

  def __init__(self, group_id=None, user_id = None, song_location_id = None, datetime=None):
    self.user_id = user_id
    self.song_location_id = song_location_id
    self.datetime = datetime

