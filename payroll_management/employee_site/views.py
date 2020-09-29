from django.shortcuts import render, redirect
from admin_site.models import EmployeeProfile, Payrolls


# Create your views here.
def employee_self_service(request):
    return render(request, 'employee_self_service.html', {})


def profile(request):
    if request.user.is_authenticated:
        username = request.user
        
        user_profile = EmployeeProfile.objects.filter(user=username)
        pay_roll = Payrolls.objects.filter(employee_name=username)

    context = {'user_profile': user_profile,
               'pay_roll': pay_roll}
    return render(request, 'profile.html', context=context)


def salary_details(request):
    if request.user.is_authenticated:
        username = request.user
        
        user_profile = EmployeeProfile.objects.filter(user=username)
        pay_roll = Payrolls.objects.filter(employee_name=username)

    context = {'user_profile': user_profile,
               'pay_roll': pay_roll}
    return render(request, 'salary_details.html', context=context)
