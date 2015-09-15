import mongoengine as mongo


class Author(mongo.Document):
    first_name = mongo.StringField(required=True)
    last_name = mongo.StringField()
    email = mongo.EmailField(required=True)
    birthdate = mongo.DateTimeField()
