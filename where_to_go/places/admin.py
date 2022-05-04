from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from places.models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['place', 'img', 'get_preview', 'number']
    readonly_fields = ('get_preview',)

    def get_preview(self, instance):
        return format_html('<img src="{}" height=200 />', instance.img.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title', ]
