from flask import request, jsonify
from functools import wraps
from flask import current_app as app  # Import app from Flask context



def require_api_key(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    api_key = request.headers.get('X-API-Key')  
    if check_api_key(api_key):
      return f(*args, **kwargs)
    else:
      return jsonify({'message': 'Invalid API key'}), 401

  return decorated_function

def check_api_key(api_key):
    FOOD_API_KEY = "GkhP0QwCUZjNSCT2qq4pAQSqodp6iVGB"
    return api_key == FOOD_API_KEY


def filter_recipes_by_dosha(recipes_list, dosha_type):
    filtered_recipes = []
    app.logger.info('Processing request for dosha type: %s', dosha_type)

    for recipe in recipes_list:
        if dosha_type == 'vata':
            if (recipe['vata_dosha_score'] > 0 and 
                recipe['vata_dosha_score'] > recipe['pitta_dosha_score'] and
                recipe['vata_dosha_score'] > recipe['kapha_dosha_score']):
                filtered_recipes.append(recipe)
        elif dosha_type == 'pitta':
            if (recipe['pitta_dosha_score'] > 0 and 
                recipe['pitta_dosha_score'] > recipe['vata_dosha_score'] and
                recipe['pitta_dosha_score'] > recipe['kapha_dosha_score']):
                filtered_recipes.append(recipe)
        elif dosha_type == 'kapha':
            if (recipe['kapha_dosha_score'] > 0 and 
                recipe['kapha_dosha_score'] > recipe['vata_dosha_score'] and
                recipe['kapha_dosha_score'] > recipe['pitta_dosha_score']):
                filtered_recipes.append(recipe)
        else:
            raise ValueError("Invalid dosha type. Choose from 'vata', 'pitta', or 'kapha'.")
    
    # Sort filtered recipes by respective dosha score and get top 20
    sorted_recipes = sorted(filtered_recipes, key=lambda x: x[f"{dosha_type}_dosha_score"], reverse=True)
    top_20_recipes = sorted_recipes[:20]

    return top_20_recipes