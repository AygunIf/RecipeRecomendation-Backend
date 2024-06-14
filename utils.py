from flask import request, jsonify
from functools import wraps


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


def filter_recipes_by_dosha(df, dosha_type):
    if dosha_type == 'vata':
        filtered_df = df[(df['vata_dosha_score'] > 0) & 
                         (df['vata_dosha_score'] > df['pitta_dosha_score']) & 
                         (df['vata_dosha_score'] > df['kapha_dosha_score'])]
        sorted_df = filtered_df.sort_values(by='vata_dosha_score', ascending=False)
    elif dosha_type == 'pitta':
        filtered_df = df[(df['pitta_dosha_score'] > 0) & 
                         (df['pitta_dosha_score'] > df['vata_dosha_score']) & 
                         (df['pitta_dosha_score'] > df['kapha_dosha_score'])]
        sorted_df = filtered_df.sort_values(by='pitta_dosha_score', ascending=False)
    elif dosha_type == 'kapha':
        filtered_df = df[(df['kapha_dosha_score'] > 0) & 
                         (df['kapha_dosha_score'] > df['vata_dosha_score']) & 
                         (df['kapha_dosha_score'] > df['pitta_dosha_score'])]
        sorted_df = filtered_df.sort_values(by='kapha_dosha_score', ascending=False)
    else:
        raise ValueError("Invalid dosha type. Choose from 'vata', 'pitta', or 'kapha'.")
    
    # Get top 20 recipes
    top_20_recipes = sorted_df.head(20).to_dict(orient='records')

    return top_20_recipes