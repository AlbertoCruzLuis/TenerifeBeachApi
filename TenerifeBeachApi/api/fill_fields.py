from flask_pymongo import ObjectId

def fill_fields(data, is_id):
    return (
        {
            '_id' : str(ObjectId(data['_id'])),
            'name' : data['name'],
            'location' : data['location'],
            'composition' : data['composition'],
            'length' : data['length']
        } if is_id else
        {
            'name' : data['name'],
            'location' : data['location'],
            'composition' : data['composition'],
            'length' : data['length']
        }
    )