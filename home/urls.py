
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.home, name = 'home'),
	path('about/', views.about, name = 'about'),
	path('service/', views.service, name = 'service'),
	path('blog/', views.blog, name = 'blog'),
]

