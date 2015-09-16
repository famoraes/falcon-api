from .models import Post
from resources import mixins


class PostController(mixins.ListMixin,
                     mixins.CreateMixin,
                     mixins.DetailMixin,
                     mixins.BaseController):
    model = Post

    def get_queryset(self):
        return Post.objects.all()

post = PostController()
