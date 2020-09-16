from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Category)
admin.site.register(models.Genre)
admin.site.register(models.Post)
admin.site.register(models.Amazon)
admin.site.register(models.Slider)
admin.site.register(models.Product)
admin.site.register(models.Testimonials)