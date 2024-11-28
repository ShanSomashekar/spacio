from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('table/<str:table_name>/', views.table_view, name='table_view'),
    path('add/<str:table_name>/', views.add_record, name='add_record'),
    path('edit/<str:table_name>/<int:pk>/', views.edit_record, name='edit_record'),
    path('delete/<str:table_name>/<int:pk>/', views.confirm_delete, name='confirm_delete'),
]
