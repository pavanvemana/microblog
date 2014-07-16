from .models import Post
from django.views.generic import ListView,DetailView


# Create your views here.
class PublishedPostsMixin(object):
    def get_queryset(self):
        queryset = super(PublishedPostsMixin, self).get_queryset()
        return queryset.filter(published=True)

class PostListView(PublishedPostsMixin,ListView):
	model = Post

class PostDetailView(PublishedPostsMixin, DetailView):
	model = Post