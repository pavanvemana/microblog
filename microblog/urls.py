from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r"^$", views.HomePageView.as_view(), name="home"),
	url(r"^blog/", include('blog.urls',namespace="blog")),
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
