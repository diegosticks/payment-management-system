from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeProfile, Payrolls


class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['user', 'first_name', 'last_name', 'department_name', 'email', 'phone_no',
                  'dob', 'city', 'state']


class EmployeePayrollForm(forms.ModelForm):
    class Meta:
        model = Payrolls
        fields = ['employee_name', 'bank_name', 'account_no', 'gross_pay']
