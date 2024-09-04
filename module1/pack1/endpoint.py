from module1 import api
from module1.pack1.resources import *

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(AddRecipe,'/receipes')
api.add_resource(Update,'/update-receipe')
api.add_resource(Delete,'/delete-receipe')
api.add_resource(Search,'/search')