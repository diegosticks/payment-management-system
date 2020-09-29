from django.contrib import admin
from .models import Department, EmployeeProfile, Payrolls

# Register your models here.
admin.site.register(Department)
admin.site.register(EmployeeProfile)
admin.site.register(Payrolls)
