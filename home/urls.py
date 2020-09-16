
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.home, name = 'home'),
	path('about/', views.about, name = 'about'),
	path('service/', views.service, name = 'service'),
	path('blog/', views.blog, name = 'blog'),
	path('contact/', views.contact, name = 'contact'),
	path('gallery/', views.gallery, name = 'gallery'),
	path('testimonials/', views.testimonials, name = 'testimonials'),
	path('faq/', views.faq, name = 'faq'),
	path('why/', views.why, name = 'why'),
	path('blog/<int:myid>/', views.blogitem, name = 'blogitem'),
]

