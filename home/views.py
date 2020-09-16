from django.shortcuts import render
from base import models

# Create your views here.

def home(request):
	template_name = 'home.html'
	context = {
		'slider' : models.Slider.objects.all().order_by('-id'),
		'about': models.Post.objects.filter(category__name = 'about'),
		'product' : models.Product.objects.all().order_by('-id'),
		'amazon' : models.Amazon.objects.get(active = True),
		'testimonials' : models.Testimonials.objects.all().order_by('-id'),
		'blog' : models.Blog.objects.all().order_by('-id'),
		'service' : models.Title.objects.get(link = 'service'),
		'products' : models.Title.objects.get(link = 'product'),
		'testimonial' : models.Title.objects.get(link = 'testimonials'),
		'blogs' : models.Title.objects.get(link = 'blog'),
	}
	return render(request, template_name, context)


def about(request):
	template_name = 'about.html'
	banner = models.Banner.objects.get(link = 'about')
	context = {
		'about': models.Post.objects.filter(category__name = 'about'),
		'team': models.Post.objects.filter(category__name = 'team').order_by('-id'),
		'amazon' : models.Amazon.objects.get(active = True),
		'banner' : banner
	}
	return render(request, template_name, context)


def service(request):
	template_name = 'service.html'
	banner = models.Banner.objects.get(link = 'service')
	context = {
		'banner' : banner
	}
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


def testimonials(request):
	template_name = 'testimonials.html'
	context = {}
	return render(request, template_name, context)


def faq(request):
	template_name = 'faq.html'
	context = {}
	return render(request, template_name, context)


def why(request):
	template_name = 'why.html'
	context = {}
	return render(request, template_name, context)


def blogitem(request, myid):
	template_name = 'singblog.html'
	blogitem = models.Blog.objects.get(id = myid)
	context = {
		'blogitem': blogitem
	}
	return render(request, template_name, context)