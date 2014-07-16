from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	#url(r"^$", views.HomePageView.as_view(), name="home"),
	url(r"^$", views.PostListView.as_view(), name="list"),
	url(r"^(?P<slug>[\w-]+)/$", views.PostDetailView.as_view(), name="detail"),
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),,
)
