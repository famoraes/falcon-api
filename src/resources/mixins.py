import json
import falcon

ERRORS_MSG = {
    404: {
        'error': 'Not found.'
    },
    405: {
        'error': 'Method not allowed.'
    }
}


class BaseController:

    def get_error_message(self, error_status):
        return json.dumps(ERRORS_MSG[error_status])

    def on_get(self, request, response, **kwargs):
        if kwargs and  hasattr(self, 'retrieve'):
            return self.retrieve(request, response, **kwargs)
        elif hasattr(self, 'list'):
            return self.list(request, response)

        response.status = falcon.HTTP_405
        response.body = self.get_error_message(405)

    def on_post(self, request, response, **kwargs):
        if kwargs and hasattr(self, 'update'):
            return self.update(request, response, **kwargs)
        elif hasattr(self, 'create'):
            return self.create(request, response)

        response.status = falcon.HTTP_405
        response.body = self.get_error_message(405)
