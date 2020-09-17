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
admin.site.register(models.Blog)
admin.site.register(models.Title)
admin.site.register(models.Banner)
admin.site.register(models.Service)
admin.site.register(models.Faq)
admin.site.register(models.Gallery)