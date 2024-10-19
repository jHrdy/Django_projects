from django.contrib import admin

# Register your models here.
from noteapp.models import *

admin.site.register(Author)
admin.site.register(Notes)

