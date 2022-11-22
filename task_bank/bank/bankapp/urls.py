from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forms/', views.forms, name='forms'),
    path('msg/', views.msg, name='msg'),
]
