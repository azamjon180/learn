
from base import models


def menu(request):
	context = {
		'genres': models.Genre.objects.all(),
		'try' : models.Title.objects.get(link = 'try'),
	}
	return context