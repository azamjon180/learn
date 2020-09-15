from django.shortcuts import render
from base import models

# Create your views here.

def home(request):
	template_name = 'home.html'
	context = {
		
	}
	return render(request, template_name, context)


def about(request):
	template_name = 'about.html'
	context = {
		'category': models.Category.objects.all()
	}
	return render(request, template_name, context)


def service(request):
	template_name = 'service.html'
	context = {}
	return render(request, template_name, context)


def blog(request):
	template_name = 'blog.html'
	context = {}
	return render(request, template_name, context)


def contact(request):
	template_name = 'contact.html'
	context = {}
	return render(request, template_name, context)


def gallery(request):
	template_name = 'gallery.html'
	context = {}
	return render(request, template_name, context)






