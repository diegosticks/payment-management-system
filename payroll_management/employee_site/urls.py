from django.urls import path
from .views import employee_self_service, profile, salary_details


app_name = 'employee_s'
urlpatterns = [
    path('employee-self-service/', employee_self_service, name='employee_self_service'),
    path('profile/', profile, name='profile'),
    path('salary-details', salary_details, name='salary-details'),
]
