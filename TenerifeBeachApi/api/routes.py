from flask import request
from flask import jsonify
from flask_restful import Resource
from flask_pymongo import ObjectId
from http import HTTPStatus
import json
from marshmallow import ValidationError
from ..database import db
from . import api
from .schemas import BeachSchema

beach_schema = BeachSchema()

class BeachList(Resource):
    def get(self):
        beaches = []
        for data in db.find():
            beaches.append({
                '_id' : str(ObjectId(data['_id'])),
                'name' : data['name'],
                'location' : data['location']
            })
        return jsonify(beaches)

    def post(self):
        try:
            beach_validated = beach_schema.load({
                'name' : request.json['name'],
                'location' : request.json['location']
            })
            id = db.insert({
                'name' : request.json['name'],
                'location' : request.json['location']
            })
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
        return jsonify({
            '_id' : str(ObjectId(beach_validated['_id'])),
            'name' : beach_validated['name'],
            'location' : beach_validated['location']
        })

    def delete(self, id):
        if not ObjectId.is_valid(id):
            return {'message' : 'Error Incorrect Id'}, 400
        beach_deleted = db.delete_one({'_id' : ObjectId(id)})
        if not beach_deleted.deleted_count:
            return {'message' : 'Error Incorrect Id'},400
        return jsonify({'message' : 'Beach Delete'})

    def put(self, id):
        if not ObjectId.is_valid(id):
            return {'message' : 'Error Incorrect Id'}, 400
        try:
            beach_validated = beach_schema.load({
            'name' : request.json['name'],
            'location' : request.json['location']
            })
            db.update_one({'_id' : ObjectId(id)}, {'$set' : {
            'name' : request.json['name'],
            'location' : request.json['location']
            }})
        except ValidationError as err:
            return err.messages,400
        
        return jsonify({'message' : 'Beach Updated'})

api.add_resource(BeachList, '/beachlist/')
api.add_resource(Beach, '/beach/<id>/')