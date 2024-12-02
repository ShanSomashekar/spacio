from django.urls import path
from .views import *
from . import views
app_name = 'employee'
urlpatterns = [
    path('login/', employee_login, name='employee_login'),
    path('create_employee/', create_employee, name='create_employee'),
    path('change_password/', change_password, name='change_password'),
path('dashboard/', employee_dashboard, name='employee_dashboard'),
    path('logout/', EmployeeLogoutView.as_view(), name='employee_logout'),



]
