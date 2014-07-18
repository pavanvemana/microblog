from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r"^$", views.PostListView.as_view(), name="list"),
	url(r"^auth/$", views.AuthView.as_view(), name="login"),
	url(r"^register/$", views.RegistrationView.as_view(), name="register"),
	url(r"^logout/$", views.Logout.as_view(), name="logout"),
	url(r"^new/$", views.PostNewView.as_view(), name="new_post"),
	#url(r"^new_post/$", views.new_post,name="post_submit"),
	url(r"^(?P<slug>[\w-]+)/$", views.PostDetailView.as_view(), name="detail"),
	url(r"^edit/(?P<slug>[\w-]+)/$", views.PostEditView.as_view(), name="edit")
	)
