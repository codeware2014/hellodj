from django.contrib import admin

# Register your models here.

from django.contrib import admin
from earthmiles import models



admin.site.register(models.User)
admin.site.register(models.User_Post)
admin.site.register(models.Snippet)

