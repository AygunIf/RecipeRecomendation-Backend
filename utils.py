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