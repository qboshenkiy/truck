from django.contrib import admin
from . models import addNews

# Register your models here.
@admin.register(addNews)
class adminNews(admin.ModelAdmin):
    list_display = ['title', 'text', 'date', 'image']