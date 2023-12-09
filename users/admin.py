from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Company, Profile, Employer, Employee

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class EmployerInline(admin.StackedInline):
    model = Employer
    can_delete = False

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, EmployerInline, EmployeeInline)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'created_at')
    search_fields = ('name', 'address', 'contact_number')
    list_filter = ('created_at',)
    inlines = [EmployerInline]

class EmployerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact_number')
    search_fields = ('full_name', 'email', 'contact_number')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact_number')
    search_fields = ('full_name', 'email', 'contact_number')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(Employee, EmployeeAdmin)
