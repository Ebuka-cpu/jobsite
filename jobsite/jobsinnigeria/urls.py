from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/latest_jobs/', views.LatestJobView.as_view(), name='latest_jobs'),
    path('', views.JobView.as_view(), name="home"),
    path('category/abuja/', views.AbujaCategoryView.as_view(), name='abuja'),
    path('category/lagos/', views.LagosCategoryView.as_view(), name='lagos'),
    path('category/plateau/', views.PlateauCategoryView.as_view(), name='plateau'),
    path('<slug:slug>/', views.JobDetailView.as_view(), name="job_detail"),
    path('job_qualification/<str:jq>/', views.JobqualifiactionView, name="job_qualification"),
    path('job_type/<str:jt>/', views.JobtypeView, name="job_type"),
    path('apply/new/', views.ApplyView.as_view(), name="apply"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
