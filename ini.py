from app import app
from model import User, db

with app.app_context():
   db.create_all()
