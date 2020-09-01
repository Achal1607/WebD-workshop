from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='users'

urlpatterns = [
path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
]