from django.contrib.messages.views import SuccessMessageMixin # generic cla
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Job, Application, Category
from .filters import JobFilter
from .forms import Applyform


class JobView(ListView):
    model = Job
    template_name = 'jobsinnigeria/home.html'
    ordering = ['-date_posted']
    context_object_name = 'jobs'
    paginate_by = 3

"""
    # search filter and latest job category filter
    def get_context_data(self, *args,  **kwargs):
        latest_cat = Job.objects.filter(published=True).order_by('-date_posted')[0:5]
        context = super(JobView, self).get_context_data(*args, **kwargs)
        context['latest_cat'] = latest_cat
        context['filter'] = JobFilter(self.request.GET, queryset=self.get_queryset())
        return context
"""

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobsinnigeria/job_detail.html'

"""
    # search filter and latest job category filter
    def get_context_data(self, **kwargs):
        latest_cat = Job.objects.filter(published=True).order_by('-date_posted')[0:5]
        context = super(JobDetailView, self).get_context_data( **kwargs)
        context['latest_cat'] = latest_cat
        return context
"""


class JobCategoryView(ListView):
    queryset = Job.objects.order_by('category')
    context_object_name = 'categories'
    template_name = 'jobsinnigeria/categories.html'


class AbujaCategoryView(ListView):
    context_object_name = 'abuja'
    queryset = Job.objects.filter(category__name="Abuja")
    template_name = 'jobsinnigeria/abuja.html'


class LagosCategoryView(ListView):
    context_object_name = 'lagos'
    queryset = Job.objects.filter(category__name="Lagos")
    template_name = 'jobsinnigeria/lagos.html'


class PlateauCategoryView(ListView):
    context_object_name = 'plateau'
    queryset = Job.objects.filter(category__name="Plateau")
    template_name = 'jobsinnigeria/plateau.html'


class LatestJobView(ListView):
    queryset = Job.objects.order_by("-date_posted")
    context_object_name = 'latest_jobs'
    paginate_by = 5
    template_name = 'jobsinnigeria/latest_jobs.html'


def JobqualifiactionView(request, jq):
    job_qualification = Job.objects.filter(job_qualification=jq)
    return render(request, 'jobsinnigeria/category_by_qualification.html', {'jq': jq.title, 'job_qualification': job_qualification})


def JobtypeView(request, jt):
    job_type = Job.objects.filter(job_type=jt)
    return render(request, 'jobsinnigeria/job_type.html', {'jt': jt.title, 'job_type': job_type})


def LatestView(request, lt):
    latest = Job.objects.filter(published=True).order_by('-date_posted')[0:5]
    return render(request, 'jobsinnigeria/latest_jobs.html', {'lt': lt.title, 'latest': latest})


class ApplyView(SuccessMessageMixin, CreateView):
    model = Application
    success_url = reverse_lazy('apply')
    template_name = 'jobsinnigeria/application_form.html'
    form_class = Applyform
    success_message = "Your Application Was Submitted"
