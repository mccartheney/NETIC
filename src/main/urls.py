from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.netics_home, name='home'),
    path("perfil/", views.profile, name='perfil')
]
