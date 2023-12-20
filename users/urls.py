from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(r'register', views.user_register),
    path(r'signin', views.user_sign_in),
    path(r'signout', views.user_sign_out),
]