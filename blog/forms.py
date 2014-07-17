from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class PostForm(forms.Form):
	widget = forms.TextInput(attrs={'class':'form-control'})
	author = forms.CharField(label='author', max_length=25,widget=widget)
	title  = forms.CharField(label='title', max_length=40,widget=widget)
	content = forms.CharField(label='content', max_length=100,widget=forms.Textarea(attrs={'class':'form-control'}))
	def clean(self):	
		if not self.cleaned_data.get('author'):
			raise ValidationError(
				"Author name can't be empty"
				)
		if not self.cleaned_data.get('title'):
			raise ValidationError(
				"Title can't be empty"
				)
		return self.cleaned_data

class AuthenticationForm(forms.ModelForm):
	widget = forms.TextInput(attrs={'class':'form-control'})
	username = forms.CharField(label="username", widget=widget)
	password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = User

	def clean(self):
		return self.cleaned_data

class RegistrationForm(forms.ModelForm):
	widget = forms.TextInput(attrs={'class':'form-control'})
	password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = ('username','email','password')
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'})
		}