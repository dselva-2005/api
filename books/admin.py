from django.contrib import admin
from .models import Book

# Register your models here.

admin.site.register(Book)

# @admin.register
# class BooksAdmin(admin.ModelAdmin):
#     list_display = ['title','subtitle','author','isbn']
#     list_filter = ['author']
