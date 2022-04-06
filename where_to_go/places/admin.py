from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Coordinates, Image


class ImageInline(admin.TabularInline):
    fields = ['img', 'get_preview', 'number']
    readonly_fields = ('get_preview',)
    model = Image

    def get_preview(self, instance):
        return format_html('<img src="{}" height=200 />'.format(instance.img.url))


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Coordinates)
admin.site.register(Image)
# Register your models here.
