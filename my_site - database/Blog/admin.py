from django.contrib import admin
from .models import Iexcel_Blog

# Register your models here.

class Iexcel_Admin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title","extract")

admin.site.register(Iexcel_Blog,Iexcel_Admin)
