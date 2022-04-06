from django.contrib import admin

from places.models import Place, Coordinates, Image


class ImageInline(admin.TabularInline):
    model = Image



class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Place, PlaceAdmin)
admin.site.register(Coordinates)
admin.site.register(Image)
# Register your models here.
