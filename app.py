from flask import Flask
from model import User, db

from services.recipe_service import *
from services.user_service import *

from utils import *

app = Flask(__name__)

#Dev Connection:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1023@localhost:5432/fooddb'

db.init_app(app)

@app.route("/")
@require_api_key
def hello_world():
    return "<p>Hello, World!</p>"



######
# Recipes
######
#@app.route('/recipes')
#@require_api_key
#def api_get_all_recipes():
#    res, status = get_all_recipes()
#    return jsonify(res), status


@app.route("/recipes/<int:id>")
@require_api_key
def api_get_recipe_by_id(id):
    res, status = get_recipe_by_id(id)
    return jsonify(res), status    


######
# User Connections
######
@app.route('/users/<string:token>')
@require_api_key
def api_get_recipe_by_token(token):
    res,status = get_user_by_token(token)
    return jsonify(res), status

@app.post('/users')
@require_api_key
def api_create_new_connection():
    res,status = create_new_connection()
    return jsonify(res), status


@app.post('/users/<string:token>/saveAnswer/<int:answer_id>')
@require_api_key
def api_save_user_answer(token, answer_id):
    res,status = add_user_answer(token,answer_id)
    return jsonify(res),status

@app.post('/users/<string:token>/save-answers')
@require_api_key
def api_save_user_answers(token):
    
    data = request.get_json()
    if len(data)<15:
        return {'message': 'No complete data provided'}, 201
    
    for d in data:
        answer_id = d['answerId']
        res,status = add_user_answer(token,answer_id)

    return jsonify(res), status

@app.put('/users/<string:token>/calculate-dosha')
@require_api_key
def api_calculate_dosha(token):
    res,status = calculate_user_dosha_type(token)
    return jsonify(res), status



if __name__ == '__main__':
    app.run(debug=True)