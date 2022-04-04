from django.contrib import admin
from to_go import views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_who_is_online, name='show_who_is_online'),
]
