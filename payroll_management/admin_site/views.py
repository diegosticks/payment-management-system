from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateForm, CreateEmployeeForm, EmployeePayrollForm
from .models import EmployeeProfile, Payrolls
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def admin_employee_manager(request):
    return render(request, 'admin_employee_manager.html', {})


def tax_filling(request):
    return render(request, 'tax/tax_filling.html', {})


def compensation(request):
    return render(request, 'compensation/compensation_admin.html', {})


def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = CreateForm()

    context = {'form': form}
    return render(request, 'create.html', context)


class EmployeeCreateView(CreateView):
    template_name = 'add_employee.html'
    form_class = CreateEmployeeForm
    queryset = EmployeeProfile.objects.all()


class EmployeeUpdateView(UpdateView):
    template_name = 'add_employee.html'
    form_class = CreateEmployeeForm
    queryset = EmployeeProfile.objects.all()


class EmployeeDeleteView(DeleteView):
    template_name = 'employee_delete.html'
    queryset = EmployeeProfile.objects.all()

    def get_success_url(self):
        return reverse('admin_s:employee-list')


class EmployeeListView(ListView):
    template_name = 'employee_list.html'
    queryset = EmployeeProfile.objects.all()


class EmployeeDetailView(DetailView):
    template_name = 'employee_details.html'
    queryset = EmployeeProfile.objects.all()


# payroll views
class EmployeeCreatePayrollView(CreateView):
    template_name = 'compensation/employee_payroll_create.html'
    form_class = EmployeePayrollForm
    queryset = Payrolls.objects.all()


class EmployeePayrollDetailView(DetailView):
    template_name = 'compensation/employee_payroll_detail.html'
    queryset = Payrolls.objects.all()


class EmployeeUpdatePayrollView(UpdateView):
    template_name = 'compensation/employee_payroll_create.html'
    form_class = EmployeePayrollForm
    queryset = Payrolls.objects.all()


class EmployeePayrollListView(ListView):
    template_name = 'compensation/employee_pay_list.html'
    queryset = Payrolls.objects.all()


class EmployeeDeletePayrollView(DeleteView):
    template_name = 'compensation/employee_payroll_delete.html'
    queryset = Payrolls.objects.all()

    def get_success_url(self):
        return reverse('admin_s:employee-pay-list')


def tex_remittance(request):
    return render(request, 'tax/statutory_remittance.html', {})
