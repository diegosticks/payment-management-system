from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from decimal import Decimal


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    phone_no = models.CharField(max_length=11)
    dob = models.DateField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('admin_s:employee-information', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Payrolls(models.Model):
    employee_name = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=10)
    gross_pay = models.DecimalField(decimal_places=2, max_digits=100000000)

    def get_absolute_url(self):
        return reverse('admin_s:employee-pay-detail', kwargs={'pk': self.pk})

    def pension(self):
        pen_total = self.gross_pay * Decimal(10/100)
        return "%.2f" % pen_total

    def paye(self):
        paye_total = self.gross_pay * Decimal(5/100)
        return "%.2f" % paye_total

    def nsitf(self):
        nsitf_total = self.gross_pay * Decimal(1/100)
        return "%.2f" % nsitf_total

    def itf(self):
        itf_total = self.gross_pay * Decimal(1/100)
        return "%.2f" % itf_total

    def nhf(self):
        nhf_total = self.gross_pay * Decimal(8/100)
        return "%.2f" % nhf_total

    def netpay(self):
        net_pay = self.gross_pay - (Decimal(self.pension()) + Decimal(self.paye()) + Decimal(self.nsitf())
                                    + Decimal(self.itf()) + Decimal(self.nhf()))
        return net_pay

    def deduct(self):
        deductions = Decimal(self.pension()) + Decimal(self.paye()) + Decimal(self.nsitf())\
                     + Decimal(self.itf()) + Decimal(self.nhf())
        return deductions
