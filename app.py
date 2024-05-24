from flask import Flask
from model import User, db

from utils import *

app = Flask(__name__)

#Dev Connection:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/fooddb'

db.init_app(app)

@app.route("/")
@require_api_key
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)