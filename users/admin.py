from django.contrib import admin
from .models import Company, Profile, Employer, Employee

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'created_at')
    search_fields = ('name', 'address', 'contact_number')
    list_filter = ('created_at',)

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact_number')
    search_fields = ('full_name', 'email', 'contact_number')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact_number')
    search_fields = ('full_name', 'email', 'contact_number')
    
admin.site.register(Company, CompanyAdmin)
admin.site.register(Profile)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Employee, EmployeeAdmin)