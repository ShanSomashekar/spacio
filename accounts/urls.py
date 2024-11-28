# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login_view, name='login'),  # URL for login view
    path('register/', views.register_view, name='register'),  # URL for register view
    path('', views.home, name='home'),  # Home URL after login
]
