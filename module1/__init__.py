import importlib
from datetime import timedelta

import redis
from flask_mysqldb import MySQL
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from redis import Redis
from flask_redis import FlaskRedis
from flask_session import Session

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://localhost:6379/0'  # Adjust according to your Redis server

app.permanent_session_lifetime = timedelta(days=1)

r = redis.Redis.from_url(app.config['REDIS_URL'])
api = Api(app)
app.config['SECRET_KEY'] = 'secret key!'



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/recipe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app, supports_credentials=True)

importlib.import_module('module1.pack1')