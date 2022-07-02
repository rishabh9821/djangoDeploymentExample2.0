from django.contrib import admin
from django.urls import path, include
from myApp import views

app_name = 'myApp'

urlpatterns = [
    path('register/', views.register, name='register'), ## View "register" function needs to be set up
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]