from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_who_is_online, name='show_who_is_online'),
]
