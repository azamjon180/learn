from django.shortcuts import render
from base import models

# Create your views here.

def home(request):
	template_name = 'home.html'
	context = {
		'slider' : models.Slider.objects.all().order_by('-id'),
		'about': models.Post.objects.filter(category__name = 'about')[0:2],
		'product' : models.Product.objects.all().order_by('-id'),
		'amazon' : models.Amazon.objects.get(active = True),
		'testimonials' : models.Testimonials.objects.all().order_by('-id'),
		'blog' : models.Blog.objects.all().order_by('-id')[0:3],
		'service' : models.Title.objects.get(link = 'service'),
		'services' : models.Service.objects.all()[0:4],
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
	services = models.Service.objects.all()
	context = {
		'banner' : banner,
		'services' : services
	}
	return render(request, template_name, context)


def blog(request):
	template_name = 'blog.html'
	banner = models.Banner.objects.get(link = 'blog')
	blog = models.Blog.objects.all().order_by('-id')
	context = {
		'banner' : banner,
		'blog' : blog
	}
	return render(request, template_name, context)


def contact(request):
	template_name = 'contact.html'
	banner = models.Banner.objects.get(link = 'contact')
	info = models.Title.objects.get(link = 'info')
	address = models.Title.objects.get(link = 'address')
	phone = models.Title.objects.get(link = 'phone')
	email = models.Title.objects.get(link = 'email')
	testi = models.Title.objects.get(link = 'testimonials')
	testis = models.Testimonials.objects.all().order_by('-id')
	context = {
		'banner' : banner,
		'info' : info,
		'address' : address,
		'phone' : phone,
		'email' : email,
		'testi' : testi,
		'testis' : testis
	}
	return render(request, template_name, context)


def gallery(request):
	template_name = 'gallery.html'
	banner = models.Banner.objects.get(link = 'gallery')
	gallerytitle = models.Title.objects.get(link = 'gallerytitle')
	gallery = models.Gallery.objects.all()
	context = {
		'banner' : banner,
		'gallerytitle' : gallerytitle,
		'gallery' : gallery
	}
	return render(request, template_name, context)


def testimonials(request):
	template_name = 'testimonials.html'
	testitle = models.Title.objects.get(link = 'happy')
	banner = models.Banner.objects.get(link = 'happy')
	testi = models.Testimonials.objects.all()
	context = {
		'testitle' : testitle,
		'banner' : banner,
		'testi' : testi
	}
	return render(request, template_name, context)


def faq(request):
	template_name = 'faq.html'
	faq = models.Faq.objects.all()
	faqtitle = models.Title.objects.get(link = 'faq')
	banner = models.Banner.objects.get(link = 'faq')
	context = {
		'faq' : faq,
		'faqtitle' : faqtitle,
		'banner' : banner
	}
	return render(request, template_name, context)


def why(request):
	template_name = 'why.html'
	banner = models.Banner.objects.get(link = 'why')
	why = models.Post.objects.filter(category__name = 'about')
	amazon = models.Amazon.objects.get(active = True)
	context = {
		'banner' : banner,
		'why' : why,
		'amazon' : amazon
	}
	return render(request, template_name, context)


def blogitem(request, myid):
	template_name = 'singblog.html'
	blogitem = models.Blog.objects.get(id = myid)
	banner = models.Banner.objects.get(link = 'blogitem')
	context = {
		'blogitem': blogitem,
		'banner' : banner
	}
	return render(request, template_name, context)