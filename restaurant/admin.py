from django.contrib import admin
from .models import UserComments, MenuItem, Category
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Category)