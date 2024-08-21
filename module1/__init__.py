import importlib

import redis as redis
from flask_redis import FlaskRedis
from flask_restful import Api
from flask import Flask

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'secret!'
app.config['REDIS_URL'] = 'redis://localhost:6379/0'  # Adjust according to your Redis server

r = redis.Redis.from_url(app.config['REDIS_URL'])

importlib.import_module('module1.pack1')