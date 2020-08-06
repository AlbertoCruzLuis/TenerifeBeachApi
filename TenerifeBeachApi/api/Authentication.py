import jwt
from flask import request, jsonify
from functools import wraps
import datetime
from ..config import DevelopmentConfig

def create_token():
    if 'username' in request.authorization:
            username = request.authorization['username']

    if 'password' in request.authorization:
        password = request.authorization['password']
    
    if username == DevelopmentConfig.USERNAME and password == DevelopmentConfig.PASSWORD:
        token = jwt.encode({username:password},DevelopmentConfig.SECRET_KEY)
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
            jwt.decode(token, DevelopmentConfig.SECRET_KEY)

        except:
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)
    return decorator