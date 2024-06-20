from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.dialects.postgresql import ARRAY

import random
import string


db = SQLAlchemy()

user_answers_table = db.Table('user_answers',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answers.answer_id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    connection_token = db.Column(db.String(12))
    dosha_type = db.Column(db.String(20), default = None)
    answers = db.relationship('Answers', secondary=user_answers_table, backref=db.backref('users', lazy='dynamic'))

    def create_connection_token(self):
        characters = string.ascii_uppercase + string.digits 
        token = ''.join(random.choice(characters) for _ in range(10))  
        self.connection_token = token
    
    def to_dict(self):
        return {
            'id':self.id,
            'connection_token': self.connection_token
            }

class Answers(db.Model):
    __tablename__ = 'answers'
    answer_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    question = db.Column(db.String(100))
    alt_letter = db.Column(db.String(1))
    alternative = db.Column(db.String(100))

    def to_dict(self):
        return {
            'answer_id':self.answer_id,
            'question': self.question,
            'alt_letter': self.alt_letter,
            'alternative': self.alternative
         }


class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key = True)
    recipe_name = db.Column(db.String(255))
    author_name = db.Column(db.String(50))
    recipe_category = db.Column(db.String(150)) #-> String
    recipe_rating = db.Column(db.Integer)#-> From 1-5
    calories = db.Column(db.Float) #Kcal
    fat_content =  db.Column(db.Float) # grams 
    saturated_fat_content = db.Column(db.Float) # grams 
    cholesterol_content =  db.Column(db.Float) # miligrams
    sodium_content = db.Column(db.Float) # miligrams 
    carbohydrate_content = db.Column(db.Float) # grams
    fiber_content = db.Column(db.Float) #grams 
    sugar_content = db.Column(db.Float) #grams 
    protein_content = db.Column(db.Float) #grams 
    recipe_servings = db.Column(db.Float)
    recipe_ingredient = db.Column(ARRAY(db.Text))  # db.Column(MutableList.as_mutable(db.PickleType))
    recipe_instructions = db.Column(ARRAY(db.Text)) # db.Column(MutableList.as_mutable(db.PickleType))
    cooktime_min = db.Column(db.Float)
    preptime_min = db.Column(db.Float)
    totaltime_min = db.Column(db.Float)
    image_url = db.Column(db.String(length=1024))
    vata_dosha_score = db.Column(db.Integer)
    pitta_dosha_score = db.Column(db.Integer)
    kapha_dosha_score = db.Column(db.Integer)
    score = db.Column(db.Float)

    def to_dict(self):
        return {
            'recipe_id': self.recipe_id,
            'recipe_name': self.recipe_name,
            'author_name': self.author_name,
            'image_url': self.image_url,
            'recipe_category': self.recipe_category,
            'recipe_rating': self.recipe_rating,
            'calories': self.calories,
            'fat_content': self.fat_content,
            'saturated_fat_content': self.saturated_fat_content,
            'cholesterol_content': self.cholesterol_content,
            'sodium_content': self.sodium_content,
            'carbohydrate_content': self.carbohydrate_content,
            'fiber_content': self.fiber_content,
            'sugar_content': self.sugar_content,
            'protein_content': self.protein_content,
            'recipe_servings': self.recipe_servings,
            'recipe_ingredient': self.recipe_ingredient,
            'recipe_instructions': self.recipe_instructions,
            'cooktime_min': self.cooktime_min,
            'preptime_min': self.preptime_min,
            'totaltime_min': self.totaltime_min,
            'vata_dosha_score': self.vata_dosha_score,
            'pitta_dosha_score': self.pitta_dosha_score,
            'kapha_dosha_score': self.kapha_dosha_score,
            'nutri_score': self.score
        }
    
    def to_dict_knn(self):
        return {
            'recipe_id': [self.recipe_id],
            'recipe_name' : [self.recipe_name],
            'author_name' : [self.author_name],
            'image_url': [self.image_url],
            'calories': [self.calories],
            'fat_content': [self.fat_content],
            'saturated_fat_content': [self.saturated_fat_content],
            'cholesterol_content': [self.cholesterol_content],
            'fiber_content': [self.fiber_content],
            'sugar_content': [self.sugar_content],
            'carbohydrate_content': [self.carbohydrate_content],
            'protein_content': [self.protein_content],
            'cooktime_min': [self.cooktime_min],
            'preptime_min': [self.preptime_min],
            'totaltime_min': [self.totaltime_min],
            'vata_dosha_score': [self.vata_dosha_score],
            'pitta_dosha_score': [self.pitta_dosha_score],
            'kapha_dosha_score' : [self.kapha_dosha_score],
            'nutri_score': [self.score]
        }