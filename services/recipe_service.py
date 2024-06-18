from model import Recipe, db
from flask import jsonify
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

    if dosha_type == 'vata':
        
        recipes = Recipe.query.filter((Recipe.vata_dosha_score>0) & 
                                  (Recipe.vata_dosha_score>Recipe.pitta_dosha_score) &
                                  (Recipe.vata_dosha_score>Recipe.kapha_dosha_score)
                                  ).order_by(Recipe.vata_dosha_score.desc()).limit(20).all()
    elif dosha_type == 'pitta':

        recipes = Recipe.query.filter((Recipe.pitta_dosha_score>0) & 
                                  (Recipe.pitta_dosha_score>Recipe.vata_dosha_score) &
                                  (Recipe.pitta_dosha_score>Recipe.kapha_dosha_score)
                                  ).order_by(Recipe.pitta_dosha_score.desc()).limit(20).all()
    elif dosha_type == 'kapha':

        recipes = Recipe.query.filter((Recipe.kapha_dosha_score>0) & 
                                  (Recipe.kapha_dosha_score>Recipe.pitta_dosha_score) &
                                  (Recipe.kapha_dosha_score>Recipe.vata_dosha_score)
                                  ).order_by(Recipe.kapha_dosha_score.desc()).limit(20).all()
    else:

         return {'message': "Invalid dosha type. Choose from 'vata', 'pitta', or 'kapha'."}, 405

    
    
    recipes_list = [recipe.to_dict() for recipe in recipes]

    return recipes_list, 200
