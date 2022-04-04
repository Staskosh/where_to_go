from django.contrib import admin

from places.models import Place, Coordinates, Image


admin.site.register(Place)
admin.site.register(Coordinates)
admin.site.register(Image)
# Register your models here.
