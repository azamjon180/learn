from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
	name = models.CharField(max_length = 50, unique = True)
	parent = TreeForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = 'children')
	link = models.CharField(max_length = 256)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length = 256)

	def __str__(self):
		return self.name