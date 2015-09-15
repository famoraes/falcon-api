import mongoengine as mongo

class Thing(mongo.Document):
    name = mongo.StringField(required=True)
    first_name = mongo.StringField()
    last_name = mongo.StringField()
