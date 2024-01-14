from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(r'register', views.user_register),
    path(r'signin', views.user_sign_in),
    path(r'signout', views.user_sign_out),
    path(r'updateInfo', views.update_user),
    path(r'user/details', views.get_user_details),
    path(r'user/followers', views.get_followers),
    path(r'user/following', views.get_following),
    path(r'user/follow', views.follow_user),
    path(r'user/unFollow/<str:username>', views.unfollow_user),
    path(r'user/getFollowers', views.get_followers),
    path(r'user/getFollowing', views.get_following),
    path(r'getUsers/<str:username>', views.get_users),
    path(r'getProfile/<str:username>', views.get_user_profile)
]
