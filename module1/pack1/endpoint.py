from module1 import api
from module1.pack1.resources import *

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(Recipes, '/recipes')
api.add_resource(UpdateRecipe, '/update-receipe/<recipe_id>')
api.add_resource(DeleteRecipe,'/delete-receipe/<recipe_id>')
api.add_resource(SearchRecipe,'/search')