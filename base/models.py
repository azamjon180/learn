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


class Post(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'category')
	title = models.TextField()
	description = models.TextField()
	content = models.TextField()
	image = models.ImageField(upload_to = 'post')
	link = models.CharField(max_length = 64, blank = True, null = True)
	active = models.BooleanField(default = False)

	def __str__(self):
		return f'{self.category} - {self.title}'


class Amazon(models.Model):
	title = models.TextField()
	description = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'amazon', null = True, blank = True)
	name_1 = models.TextField(null = True, blank = True)
	number_1 = models.DecimalField(max_digits = 8, decimal_places = 2, null = True, blank = True)
	name_2 = models.TextField(null = True, blank = True)
	number_2 = models.DecimalField(max_digits = 8, decimal_places = 2, null = True, blank = True)
	name_3 = models.TextField(null = True, blank = True)
	number_3 = models.DecimalField(max_digits = 8, decimal_places = 2, null = True, blank = True)
	link = models.CharField(max_length = 64, blank = True, null = True)
	active = models.BooleanField(default = False)

	def __str__(self):
		return self.title


class Slider(models.Model):
	title = models.TextField()
	description = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'slider')
	link = models.CharField(max_length = 64, null = True, blank = True)
	active = models.BooleanField(default = False)

	def __str__(self):
		return self.title


class Product(models.Model):
	name = models.TextField()
	description = models.TextField(null = True, blank = True)
	content = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'product')
	link = models.CharField(max_length = 64, null = True, blank = True)
	active = models.BooleanField(default = False)

	def __str__(self):
		return self.name


class Testimonials(models.Model):
	name = models.CharField(max_length = 256)
	description = models.TextField(null = True, blank = True)
	image = models.ImageField(upload_to = 'testimonials')
	link = models.CharField(max_length = 64, null = True, blank = True)
	active = models.BooleanField(default = False)

	def __str__(self):
		return self.name

		