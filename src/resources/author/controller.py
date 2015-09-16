import falcon
import datetime

from .models import Author
from resources import mixins


class AuthorController(mixins.ListMixin,
                       mixins.DetailMixin,
                       mixins.BaseController):
    model = Author

    def _deserialize(self, data):
        if data.get('birthdate'):
            data['birthdate'] = datetime.datetime.strptime(data['birthdate'], '%Y/%m/%d')

        return data

    def get_queryset(self):
        return self.model.objects.all()

    def create(self, request, response):
        data = self._deserialize(request.context['data'])
        author = Author(**data).save()
        response.body = author.to_json()
        response.status = falcon.HTTP_201

author = AuthorController()
