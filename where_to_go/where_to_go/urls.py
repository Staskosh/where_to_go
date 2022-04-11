from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from places import views

import tinymce.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_places, name='show_places'),
    path('places/<int:place_id>/', views.place_detail_view, name='place_detail_view'),
    path('tinymce/', include('tinymce.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)