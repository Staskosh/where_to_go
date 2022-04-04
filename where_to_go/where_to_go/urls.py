from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_who_is_online, name='show_who_is_online'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)