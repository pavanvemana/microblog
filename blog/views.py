from .models import Post
from django.conf import settings
from django.views.generic import ListView,DetailView,TemplateView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from django.shortcuts import render, render_to_response
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout,authenticate
from django.views.decorators.debug import sensitive_post_parameters
from django.template import RequestContext


# Create your views here.
class PublishedPostsMixin(object):
    def get_queryset(self):
        queryset = super(PublishedPostsMixin, self).get_queryset()
        return queryset.filter(published=True)

class PostListView(PublishedPostsMixin,ListView):
	model = Post
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PostListView, self).dispatch(*args, **kwargs)


class PostDetailView(PublishedPostsMixin, DetailView):
	model = Post
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PostDetailView, self).dispatch(*args, **kwargs)

class PostNewView(FormView):
	model = Post
	#template_name = 'blog/new.html'
	form_class = forms.PostForm
	def get(self, request, *args, **kwargs):
		form = forms.PostForm()
		return render(request, 'blog/new.html', {'form': form})
	def post(self, request, *args, **kwargs):
		form = forms.PostForm(request.POST)
		if form.is_valid():
			author = User.objects.create_user(username=form.cleaned_data['author'],password='tarams123')
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			created_at = timezone.now()
			updated_at = timezone.now()
			Post.objects.create(author=author, title=title, created_at=created_at, updated_at=updated_at, content=content)
			return HttpResponseRedirect(reverse('blog:list'))
		return render(request, 'blog/new.html', {'form': form})

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(PostNewView, self).dispatch(*args, **kwargs)



class AuthView(FormView):
	form_class = forms.AuthenticationForm

	#template_name = 'blog/auth.html'
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return HttpResponseRedirect('/blog/')
		else:
			form = forms.AuthenticationForm
			context = RequestContext(request,{
				'form':form,
				'next':request.GET['next']
				})
			return render(request,'blog/auth.html', context)

	def post(self, request,*args, **kwargs):
		form = forms.AuthenticationForm
		context = RequestContext(request)
		username = request.POST['username']
		password = request.POST['password']
		#redirect_to = request.POST['next']

		user = authenticate(username=username,password=password)
		if user:
			auth_login(request,user)
			return HttpResponseRedirect(request.POST.get('next',None))
		else:
			#return HttpResponse("Invalid login details supplied")
			return render_to_response('blog/auth.html',{'form':form},context)
	
		
class RegistrationView(FormView):
	form_class = forms.RegistrationForm
	def get(self,request,*args,**kwargs):
		form = forms.RegistrationForm
		return render(request,'blog/register.html',{'form':form})
	
	def post(self,request,*args,**kwargs):
		form = forms.RegistrationForm(request.POST)
		context = RequestContext(request)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			User.objects.create_user(username=username,password=password,email=email)
			return HttpResponseRedirect(reverse('blog:list'))
		else:
			return render_to_response('blog/register.html', {'form': form},context)

class Logout(FormView):
	def get(self, request, *args, **kwargs):
		auth_logout(request)
		return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)

def new(request):
	if request.method == 'POST':
		form = forms.PostForm(request.POST)
		if form.is_valid():
			author = User.objects.create_user(username=form.cleaned_data['author'],password='tarams123')
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			created_at = timezone.now()
			updated_at = timezone.now()
			Post.objects.create(author=author, title=title, created_at=created_at, updated_at=updated_at, content=content)
			return HttpResponseRedirect(reverse('blog:list'))
	
	else:
		form = forms.PostForm()
	
	return render(request, 'blog/new.html', {'form': form})
