import django_filters
from django.db.models import Q

from .models import Job


class JobFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='my_custom_filter', label='Search')

    class Meta:
        model = Job
        fields = ['search']

    def my_custom_filter(self, queryset, name, value):
        return Job.objects.filter(
            Q(job_title__icontains=value) | Q(job_location__icontains=value) | Q(job_qualification__icontains=value)
        )
