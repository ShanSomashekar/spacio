from django.urls import path

from . import views
from .views import view_tables, list_records

urlpatterns = [
    path('', view_tables, name='view_tables'),
    path('<str:table_name>/list/', views.list_records, name='list_records'),
    path('<str:table_name>/edit/<int:id>/', views.edit_record, name='edit_record'),
    path('<str:table_name>/add/', views.add_record, name='add_record'),
    path('<str:table_name>/delete/<int:id>/', views.delete_record, name='delete_record'),
]
