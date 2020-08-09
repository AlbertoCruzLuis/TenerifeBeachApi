from flask import request
from flask import jsonify
from flask_restful import Resource
from flask_pymongo import ObjectId
from http import HTTPStatus
import json
from marshmallow import ValidationError
from ..database import db
from . import api
from .fill_fields import fill_fields
from .schemas import BeachSchema
from .Authentication import token_required, create_token

beach_schema = BeachSchema()

class Authentication(Resource):
    def post(self):
        return create_token()

class BeachList(Resource):
    def get(self):
        beaches = []
        for data in db.find():
            beaches.append(fill_fields(data,True))
        return jsonify(beaches)

    @token_required
    def post(self):
        try:
            beach_schema.load(fill_fields(request.json,False))
            id = db.insert(fill_fields(request.json,False))
        except ValidationError as err:
            return err.messages,400
        return jsonify(str(ObjectId(id)))

class Beach(Resource):
    def get(self, id):
        if not ObjectId.is_valid(id):
            return {'message' : 'Error Incorrect Id'}, 400
        beach = db.find_one_or_404({ '_id' : ObjectId(id)})
        try:
            beach_validated = beach_schema.load(beach)
        except ValidationError as err:
            return err.messages,400
        return jsonify(fill_fields(beach_validated,True))

    @token_required
    def delete(self, id):
        if not ObjectId.is_valid(id):
            return {'message' : 'Error Incorrect Id'}, 400
        beach_deleted = db.delete_one({'_id' : ObjectId(id)})
        if not beach_deleted.deleted_count:
            return {'message' : 'Error Incorrect Id'},400
        return jsonify({'message' : 'Beach Delete'})

    @token_required
    def put(self, id):
        if not ObjectId.is_valid(id):
            return {'message' : 'Error Incorrect Id'}, 400
        try:
            beach_schema.load(fill_fields(request.json,False))
            db.update_one({'_id' : ObjectId(id)}, {'$set' : fill_fields(request.json,False)})
        except ValidationError as err:
            return err.messages,400
        
        return jsonify({'message' : 'Beach Updated'})

api.add_resource(BeachList, '/beachlist/')
api.add_resource(Beach, '/beach/<id>/')
api.add_resource(Authentication, '/auth/')