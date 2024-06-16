from model import Recipe, db
from flask import jsonify
from utils import filter_recipes_by_dosha
from flask import current_app as app  # Import app from Flask context



def get_all_recipes():
    all_recipes = Recipe.query.limit(20).all()
    recep_list = [recipe.to_dict() for recipe in all_recipes]
    return (recep_list), 200

def get_recipe_by_id(id):
    recep = Recipe.query.get(id)
    if recep is None:
        return {'message': 'Recipe not found.'}, 404
    return recep.to_dict(), 200

def get_recipe_by_dosha_type(dosha_type):
    
    recipes = Recipe.query.all()
    app.logger.info('Hello. Processing default request')

    recipes_list = [recipe.to_dict() for recipe in recipes]

    filtered_recipes = filter_recipes_by_dosha(recipes_list, dosha_type)
    if filtered_recipes is None:
         return {'message': 'No recipes for provided dosha type.'}, 404
    return filtered_recipes, 200
