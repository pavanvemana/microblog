from django.views.generic import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
	template_name = "blog/index.html"

def view_404(request):
	return render(request,'blog/400.html')

def view_500(request):
	return render(request,'blog/500.html')