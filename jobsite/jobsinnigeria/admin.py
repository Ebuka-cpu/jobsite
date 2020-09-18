from django.contrib import admin

from .models import Job, Application, JobCategory


class JobInline(admin.StackedInline):
    model = Job
    extra = 1

class JobAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'job_type', 'job_location', 'job_author', 'category', 'published']


class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [JobInline]

admin.site.register(Job, JobAdmin)
admin.site.register(Application)
admin.site.register(JobCategory, JobCategoryAdmin)
