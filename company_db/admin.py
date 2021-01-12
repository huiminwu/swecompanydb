from django.contrib import admin
from .models import Company, CompanyRep

admin.site.site_header = 'MIT SWE Company Database'
admin.site.site_title = 'Admin Page'
admin.site.index_title = 'Database administration'

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name', ]

@admin.register(CompanyRep)
class CompanyRepAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'role')
    list_filter = ('active', 'main', 'role', 'company')
    search_fields = ['name', ]
