import requests as requests
from flask_restful import Resource
from flask import render_template, make_response, request, jsonify, redirect, session

from module1 import r


class Register(Resource):
    def get(self):
        return make_response(render_template('register.html'))

    def post(self):

        data = {
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password'],

        }

        response = requests.post('http://127.0.0.1:8001/register', json=data)

        if response.status_code == 200:

            return redirect('http://127.0.0.1:8000/login')

            # return response.json()  # Return response from the database microservice
        else:
            return make_response(jsonify({"error": "Failed to insert data into the database"}), 500)


class Login(Resource):
    def get(self):
        return make_response(render_template('login.html'))

    def post(self):
        data = {
            "email": request.form['email'],
            "password": request.form['password']
        }

        response = requests.post('http://127.0.0.1:8001/login', json=data)

        if response.status_code == 200:
            return redirect('recipes')
        else:
            return make_response("Failed to login")


class Recipes(Resource):
    def get(self):
        response = requests.get('http://127.0.0.1:8001/receipes')

        if response.status_code == 200:
            data = response.json()['recipes']
            return make_response(render_template('receipes.html', recipes=data))

    def post(self):
        data = {
            "rname": request.form['receipe_name'],
            "rdec": request.form['receipe_des']
        }

        response = requests.post('http://127.0.0.1:8001/receipes', json=data)

        if response.status_code == 200:
            data = response.json()['recipes']
            return make_response(render_template('receipes.html', recipes=data))


class UpdateRecipe(Resource):
    def get(self, recipe_id):
        session['recipe_id'] = recipe_id
        return make_response(render_template('update_reciepes.html'))

    def post(self, recipe_id):
        print(recipe_id)
        recipe_id = session.get('recipe_id')

        if not recipe_id:
            return {'message': 'Recipe ID not found'}, 400

        receipe_name = request.form.get('receipe_name')
        receipe_des = request.form.get('receipe_des')

        if not receipe_name or not receipe_des:
            return {'message': 'Recipe name and description are required'}, 400

        data = {
            "recipe_id": recipe_id,
            "receipe_name": receipe_name,
            "receipe_des": receipe_des
        }

        # Make request to update endpoint
        response = requests.post('http://127.0.0.1:8001/update-receipe', json=data)

        if response.status_code == 200:
            return redirect('http://127.0.0.1:8000/recipes')
        else:
            return {'message': 'Failed to update recipe'}, response.status_code


class DeleteRecipe(Resource):
    def get(self, recipe_id):
        data = {
            'recipe_id': recipe_id
        }
        response = requests.post('http://127.0.0.1:8001/delete-receipe', json=data)
        if response.status_code == 200:
            return redirect('http://127.0.0.1:8000/recipes')
        else:
            return {'message': 'Failed to delete recipe'}


class SearchRecipe(Resource):
    def get(self):
        return make_response(render_template('search.html'))
    def post(self):
        receipe_name = request.form.get('search')
        data = {
            "receipe_name": receipe_name,
        }
        response = requests.post('http://127.0.0.1:8001/search', json=data)

        data = response.json()['recipes']
        return make_response(render_template('receipes.html', recipes=data))
