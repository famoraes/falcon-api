import mongoengine as mongo

from resources.author.models import Author


class Post(mongo.Document):
    author = mongo.ReferenceField(Author)
    title = mongo.StringField(required=True, max_length=300)
    text = mongo.StringField(required=True)
