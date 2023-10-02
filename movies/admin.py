from django.contrib import admin
from .models import Movie
# Register your models here.

@admin.register(Movie)
class reg1(admin.ModelAdmin):
    list_display = ['id','title','genre','release_date','director']
