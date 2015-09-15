import falcon
import datetime

from .models import Author
from resources.mixins import BaseController


class AuthorController(BaseController):

    def _deserialize(self, data):
        if data.get('birthdate'):
            data['birthdate'] = datetime.datetime.strptime(data['birthdate'], '%Y/%m/%d')

        return data

    def list(self, request, response):
        response.status = falcon.HTTP_200
        response.body = Author.objects.all().to_json()

    def retrieve(self, request, response, **kwargs):
        author_id = kwargs.pop('author_id')
        author = Author.objects(id=author_id)

        if author:
            response.status = falcon.HTTP_200
            response.body = author.to_json()
        else:
            response.status = falcon.HTTP_404
            response.body = self.get_error_message(404)

    def create(self, request, response):
        data = self._deserialize(request.context['data'])
        author = Author(**data).save()
        response.body = author.to_json()
        response.status = falcon.HTTP_201

author = AuthorController()
