from django.contrib import admin
from .models import candidate, company, jobposttable, candidatedetail

@admin.register(candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'contatct', 'city', 'state', 'dob', 'gender')
    search_fields = ('firstname', 'lastname', 'city', 'state')
    list_filter = ('state', 'city', 'gender')

@admin.register(company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'firstname', 'lastname', 'state', 'city', 'contact')
    search_fields = ('company_name', 'city', 'state')
    list_filter = ('state', 'city')

@admin.register(jobposttable)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'jobname', 'companyname', 'expirience', 'salary', 'qulification', 'email', 'contact')
    search_fields = ('jobname', 'companyname', 'qulification')
    list_filter = ('expirience', 'salary', 'qulification')

@admin.register(candidatedetail)
class CandidateDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'qulification', 'contact')
    search_fields = ('name', 'email', 'qulification')
    list_filter = ('qulification',)
