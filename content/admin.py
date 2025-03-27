from django.contrib import admin

# Register your models here.

from .models import Band, Genre, Singer

admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Singer)