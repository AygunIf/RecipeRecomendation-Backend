from model import Recipe, db
from flask import jsonify
from flask import current_app as app  # Import app from Flask context

import joblib
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np

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

def get_recommended_recipes(recipe_id):
    
    knn = joblib.load('data/knn_model.pkl')
    y_np = np.load('data/train_label.npy', allow_pickle=True)

    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    #test recipe: 323

    if recipe is None:
        return {'message': 'Recipe not found.'}, 404

    example_profile = pd.DataFrame(recipe.to_dict_knn())
    print(example_profile.columns)
    y_val = example_profile.filter(['recipe_id','recipe_name'])
    X_val = example_profile.drop(['recipe_id', 'recipe_name', 'score'], axis=1) # after training remove score from the list
                                                                                #error: "message": "Error in KNN prediction: X has 15 features, but NearestNeighbors is expecting 14 features as input."

    
    X_val = X_val.values
    y_val = y_val.values
    
    try:
        distances, index = knn.kneighbors(X_val)
    except Exception as e:
        return {'message': f'Error in KNN prediction: {str(e)}'}, 500

    recommended_recipes = [{'recipe_id' : y_np[i][0], 'recipe_name': y_np[i][1] } for i in index[0]]

    return recommended_recipes, 200