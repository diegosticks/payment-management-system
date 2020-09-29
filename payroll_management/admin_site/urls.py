from django.urls import path
from .views import (admin_employee_manager, compensation,
                    tax_filling, create, EmployeeUpdateView,
                    EmployeeCreateView, EmployeeDeleteView,
                    EmployeeDetailView, EmployeeListView,
                    EmployeeCreatePayrollView, EmployeePayrollDetailView,
                    EmployeeUpdatePayrollView, EmployeePayrollListView,
                    EmployeeDeletePayrollView, tex_remittance)


app_name = 'admin_s'
urlpatterns = [
    path('admin-manager/', admin_employee_manager, name='admin_employee_manager'),
    path('compensation-admin/', compensation, name='compensation_admin'),
    path('tax-filling/', tax_filling, name='tax_filling'),
    path('create/', create, name='create'),
    path('create-employee/', EmployeeCreateView.as_view(), name='create-employee'),
    path('profile-list/', EmployeeListView.as_view(), name='employee-list'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee-information'),
    path('<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),

    path('create-employee-payroll/', EmployeeCreatePayrollView.as_view(), name='create-employee-payroll'),
    path('employee-pay-details/<int:pk>/employee-pay-details', EmployeePayrollDetailView.as_view(), name='employee-pay-detail'),
    path('employee-pay-details/<int:pk>/update/', EmployeeUpdatePayrollView.as_view(), name='employee-pay-update'),
    path('employee-pay-details/<int:pk>/delete/', EmployeeDeletePayrollView.as_view(), name='employee-pay-delete'),
    path('employee-pay-list/', EmployeePayrollListView.as_view(), name='employee-pay-list'),

    path('statutory-remittance/', tex_remittance, name='tax-remittance'),
]
