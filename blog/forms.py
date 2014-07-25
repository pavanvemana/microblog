from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.Form):
	widget = forms.TextInput(attrs={'class':'form-control'})
	widget_author = forms.TextInput(attrs={'class':'form-control','readonly':True})
	author = forms.CharField(label='author', max_length=25,widget=widget_author)
	title  = forms.CharField(label='title', max_length=40,widget=widget, help_text='Your post title')
	content = forms.CharField(label='content', max_length=100,widget=forms.Textarea(attrs={'class':'form-control','rows':5}))
	files = forms.FileField(label='Add File', required=False)

class AuthenticationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','password')
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'password':forms.TextInput(attrs={'class':'form-control'})
		}
	def clean(self):
		return self.cleaned_data


class RegistrationForm(forms.ModelForm):
	email = forms.CharField(max_length=128,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ('username','email','password')
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'password':forms.TextInput(attrs={'class':'form-control'}),
		}

class PostEditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','slug','content','published')
		widget = forms.TextInput(attrs={'class':'form-control'})
		widgets = {
			'title':widget, 'slug':widget,'content':forms.Textarea(attrs={'class':'form-control','rows':5})
		}