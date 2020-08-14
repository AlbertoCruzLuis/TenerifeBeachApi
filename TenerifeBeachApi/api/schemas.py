from marshmallow import Schema, fields, validate, ValidationError, INCLUDE

class BeachSchema(Schema):
    _id = fields.Str(dump_only=True)
    name = fields.Str(validate=validate.Length(min=1))
    location = fields.Str(validate=validate.Length(min=1))
    composition = fields.Str(validate=validate.Length(min=1))
    length = fields.Int(validate=validate.Range(min=1, max=99999))
    image = fields.Str(validate=validate.Length(min=1))

    class Meta:
        unknown = INCLUDE