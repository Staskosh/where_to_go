from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

from to_go import views
from where_to_go import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_who_is_online, name='show_who_is_online'),
]
