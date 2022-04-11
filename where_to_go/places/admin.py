from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html


from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ['title', 'img', 'get_preview', 'number']
    readonly_fields = ('get_preview',)

    def get_preview(self, instance):
        return format_html('<img src="{}" height=200 />'.format(instance.img.url))


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title',]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
# Register your models here.
