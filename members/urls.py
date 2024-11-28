from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),

path('create-booking/', views.create_booking, name='create_booking'),
path('coworking-space/', views.coworking_space, name='coworking_space'),
    path('book-space/', views.book_space, name='book_space'),
]
