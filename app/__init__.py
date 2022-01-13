from flask import Flask
from app.database.ramdb import Ramdb
from app.models.cinema import Hall_repo, Movie_repo, Session_repo

app = Flask(__name__)
DB = Ramdb()
HALL_REPO = Hall_repo(DB)
MOVIE_REPO = Movie_repo(DB)
SESSION_REPO = Session_repo(DB)

from app import views