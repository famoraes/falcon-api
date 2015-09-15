import falcon

from .models import Post
from resources.mixins import BaseController


class PostController(BaseController):

    def list(self, request, response):
        response.status = falcon.HTTP_200
        response.body = Post.objects.all().to_json()

post = PostController()
