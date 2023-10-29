from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'created_at')
    search_fields = ('name', 'address', 'contact_number')
    list_filter = ('created_at',)

admin.site.register(Company, CompanyAdmin)