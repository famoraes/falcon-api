import falcon
import mongoengine as mongo

# Resources
from resources.post.controller import post
from resources.author.controller import author

# Middleware
import middlewares

# Init falcon app
app = falcon.API(middleware=[
    middlewares.JSONTranslator()
])

# DB
mongo.connect('admin')

# Routes
app.add_route('/authors', author)
app.add_route('/authors/{author_id}', author)
app.add_route('/posts', post)
app.add_route('/posts/{post_id}', post)
