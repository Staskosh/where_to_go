from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from places.models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['title', 'img', 'get_preview', 'number']
    readonly_fields = ('get_preview',)

    def get_preview(self, instance):
        return format_html(mark_safe('<img src="{}" height=200 />'), instance.img.url)


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title', ]


admin.site.register(Place, PlaceAdmin)
