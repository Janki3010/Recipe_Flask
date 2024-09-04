import base64
import json
import os

from flask import request, session
from flask_restful import Resource

from module1 import db, r
from module1.pack1.model import *


class Register(Resource):
    def post(self):
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        new_user = User(username=username, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()

        return {"message": "Data inserted successfully"}, 200


class Login(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        user1 = User.query.filter_by(email=email, password=password).first()

        if user1:
            # session['user_id'] = user1.id
            r.set('user_id', user1.id)
            return {"message": "Successful login"}, 200
        else:
            return {"error": "Invalid email or password"}, 401


class AddRecipe(Resource):
    def get(self):
        all_recipes = UserReceipe.query.all()
        recipes_list = []
        for recipe in all_recipes:
            recipes_list.append({
                'id': recipe.id,
                'user_id': recipe.user_id,
                'receipe_name': recipe.receipe_name,
                'receipe_des': recipe.receipe_des
            })

        return {'msg': 'Success',
                'recipes': recipes_list}, 200

    def post(self):
        data = request.json
        receipe_name = data.get('rname')
        receipe_des = data.get('rdec')
        # user_id = session.get('user_id')
        uid = r.get('user_id')

        if uid is None:
            return {"error": "User not logged in"}, 401

        recipe = UserReceipe(user_id=uid, receipe_name=receipe_name, receipe_des=receipe_des)

        db.session.add(recipe)
        db.session.commit()

        all_recipes = UserReceipe.query.all()
        recipes_list = []
        for recipe in all_recipes:
            recipes_list.append({
                'id': recipe.id,
                'user_id': recipe.user_id,
                'receipe_name': recipe.receipe_name,
                'receipe_des': recipe.receipe_des
            })

        print(recipes_list)

        return {'msg': 'Success',
                'recipes': recipes_list}, 200


class Update(Resource):
    def post(self):
        data = request.json
        recipe_id = data.get('recipe_id')
        receipe_name = data.get('receipe_name')
        receipe_des = data.get('receipe_des')

        # recipe = UserReceipe.query.filter_by(id).first()
        recipe = UserReceipe.query.get(recipe_id)
        if recipe:
            recipe.receipe_name = receipe_name
            recipe.receipe_des = receipe_des
            db.session.commit()


class Delete(Resource):
    def post(self):
        data = request.json
        id = data.get('recipe_id')
        recipe = UserReceipe.query.get(id)
        if not recipe:
            return {'message': 'Recipe not found'}, 404

        db.session.delete(recipe)
        db.session.commit()


class Search(Resource):
    def post(self):
        data = request.json
        name = data.get('receipe_name')

        # recipe = UserReceipe.query.get(name)
        recipes = UserReceipe.query.filter(
            db.or_(
                UserReceipe.receipe_name.like(f'%{name}%')
            )
        ).all()
        recipes_list = []
        for recipe in recipes:
            recipes_list.append({
                'id': recipe.id,
                'user_id': recipe.user_id,
                'receipe_name': recipe.receipe_name,
                'receipe_des': recipe.receipe_des
            })
        return {'msg': 'Success',
                'recipes': recipes_list}, 200
