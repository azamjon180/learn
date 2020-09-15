
from base import models


def menu(request):
	context = {
		'genres': models.Genre.objects.all()
	}
	return context