import falcon
import mongoengine as mongo

# Resources
from resources.things.controller import things

# Middleware
import middlewares

# Init falcon app
app = falcon.API(middleware=[
    middlewares.JSONTranslator()
])

# DB
mongo.connect('admin')

# Routes
app.add_route('/things', things)
