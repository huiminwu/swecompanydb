from django.contrib import admin
from .models import Company, CompanyRep

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

@admin.register(CompanyRep)
class CompanyRepAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'role')
    list_filter = ('active', 'main', 'company')
    search_fields = ['name', ]
