from bs4 import BeautifulSoup

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from autoslug import AutoSlugField
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = 'Categories'


class Job(models.Model):
    job_title = models.CharField(max_length=250, blank=True, null=True)
    slug = AutoSlugField(populate_from='job_title', unique=True, 
							always_update=False, default='')
    job_author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    job_description = HTMLField()
    job_type = models.CharField(max_length=250, blank=True, null=True)
    job_location = models.CharField(max_length=250, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    about_the_company = HTMLField()
    qualifications = models.CharField(max_length=400, blank=True, null=True)
    competency_title = models.CharField(max_length=20, blank=True, default='competency')
    competency = models.TextField(blank=True, default=None)
    job_requirements = HTMLField()
    website = models.URLField(max_length=250, null=True, blank=True)
    job_experience = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey(Category, max_length=20, blank=True, null=True, default="Lagos",
                                 on_delete = models.DO_NOTHING)
    published = models.BooleanField(default=True)
    job_qualification = models.CharField(max_length=250, blank=True, null=True, default="bsc")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug": self.slug})

    def html_to_text(self, *args, **kwargs):
        soup = BeautifulSoup(self.content, features="html.parser")
        text = soup.get_text()
        return text


class Age(models.TextChoices):
    Sixteen = "16"
    Seventeen = "17"
    Eighteen = "18"
    Nineteen = "19"
    Twenty = "20"
    

class Application(models.Model):
    GENDER = (
        ("Male", "MALE"),
        ("Female", "FEMALE")
    )
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    age = models.CharField(choices=Age.choices, default=Age.Sixteen, max_length=20)
    gender = models.CharField(choices=GENDER, default="Male", max_length=6)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(default=timezone.now)
    cv = models.FileField(upload_to="cv")

    def __str__(self):
        return self.firstname
