from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Organization)
admin.site.register(models.Residency)
admin.site.register(models.Offer)
admin.site.register(models.Required)
admin.site.register(models.Image)
admin.site.register(models.Video)