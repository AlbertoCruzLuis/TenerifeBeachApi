import jwt
from flask import request, jsonify
from functools import wraps
import datetime
from ..config import ProductionConfig

Config = ProductionConfig

def create_token():
    if 'username' in request.authorization:
            username = request.authorization['username']

    if 'password' in request.authorization:
        password = request.authorization['password']
    
    if username == Config.USERNAME and password == Config.PASSWORD:
        token = jwt.encode({username:password},Config.SECRET_KEY)
        return jsonify({'token':token.decode()})
    return jsonify({'message' : "You don't have authorization"})

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None        

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': "You don't have authorization"})

        try:
            jwt.decode(token, Config.SECRET_KEY)

        except:
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)
    return decorator