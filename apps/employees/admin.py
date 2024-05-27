from django.contrib import admin

from .models import Employee


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(Employee)

