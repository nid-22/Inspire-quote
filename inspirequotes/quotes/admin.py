from django.contrib import admin

# Register your models here.
from .models import quotes,author,category,movie

class quotes_admin(admin.ModelAdmin):
    list_display=['line','category','movie','author']
    list_filter=[]

class author_admin(admin.ModelAdmin):
    list_display=['name','birthdate']
    list_filter=[]

class category_admin(admin.ModelAdmin):
    list_display=['name']
    list_filter=[]

class movie_admin(admin.ModelAdmin):
    list_filter=[]


admin.site.register(quotes,quotes_admin)
admin.site.register(author,author_admin)
admin.site.register(category,category_admin)
admin.site.register(movie,movie_admin)
