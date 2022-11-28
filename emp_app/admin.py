from django.contrib import admin
from emp_app.models import employee,department,role

# Register your models here.
admin.site.register(employee)
admin.site.register(department)
admin.site.register(role)
