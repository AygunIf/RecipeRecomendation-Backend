from flask_sqlalchemy import SQLAlchemy

import random
import string


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    connection_token = db.Column(db.String(12))

    def create_connection_token(self):
        characters = string.ascii_uppercase + string.digits 
        token = ''.join(random.choice(characters) for _ in range(10))  
        self.connection_token = token


class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    prep_time = db.Column(db.String(25)) #TimeInterval 
    total_time = db.Column(db.String(25)) #TimeInterval 
    saturated_fat_content = db.Column(db.Float) # grams 
    cholesterol_content =  db.Column(db.Float) # miligrams
    sodium_content = db.Column(db.Float) # miligrams 
    carbohydrate_content = db.Column(db.Float) # grams
    fiber_content = db.Column(db.Float) #grams 
    sugar_content = db.Column(db.Float) #grams 
    protein_content = db.Column(db.Float) #grams 
    recipe_servings = db.Column(db.Float)
    calories = db.Column(db.Float) #Kcal
    rating = db.Column(db.Integer)#-> From 1-5
    recipe_category = db.Column(db.Integer) #-> String
    source = db.Column(db.String(20))
    

    def to_dict(self):
        return {
            'recipe_id': self.recipe_id,
            'name': self.name,
            'prep_time': self.prep_time,
            'total_time': self.total_time,
            'saturated_fat_content': self.saturated_fat_content,
            'cholesterol_content': self.cholesterol_content,
            'sodium_content':self.sodium_content,
            'carbohydrate_content': self.carbohydrate_content,
            'fiber_content': self.fiber_content,
            'sugar_content': self.sugar_content,
            'protein_content':self.protein_content,
            'recipe_servings':self.recipe_servings,
            'calories':self.calories,
            'rating' : self.rating,
            'recipe_category':self.recipe_category,
            'source': self.source
        }    
    
    