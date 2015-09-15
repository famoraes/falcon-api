import falcon

from .models import Thing

class Things:

    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = Thing.objects.all().to_json()

    def on_post(self, request, response):
        data = request.context['data']
        thing = Thing(**data)
        response.body = thing.to_json()

things = Things()
