from django.contrib import admin
from . import models

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_joined')
    ordering = ('-date_joined',)

admin.site.register(models.Customer, CustomerAdmin)

