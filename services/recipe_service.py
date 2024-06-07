from model import Recipe, db

def get_all_recipes():
    all_recipes = Recipe.query.limit(20).all()
    recep_list = [recipe.to_dict() for recipe in all_recipes]
    return (recep_list), 200

def get_recipe_by_id(id):
    recep = Recipe.query.get(id)
    if recep is None:
        return {'message': 'Recipe not found.'}, 404
    return recep.to_dict(), 200