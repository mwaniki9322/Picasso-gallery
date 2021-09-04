from datetime import date
from django.contrib import admin
from . models import Image,Locations,Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('Locations','Category')

admin.site.register(Image)
admin.site.register(Locations)
admin.site.register(Category)
