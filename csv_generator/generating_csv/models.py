import os

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.


class DataScheme(models.Model):
    SEPARATOR = (
        (',', 'Comma (,)'),
        ('.', 'Semicolon (;)'),
        ('|', 'Pipe (|)'),
    )
    QUALIFIER = (
        ('"', 'Double quotes("..")'),
        ("'", "Single quotes ('..')"),
    )

    def scheme_upload_to(self, instance=None):
        if instance:
            return os.path.join("DataScheme", slugify(self.slug), instance)

    class Meta:
        verbose_name = "Data Scheme"
        verbose_name_plural = "Data Schemes"
        ordering = ["-date_updated"]

    title = models.CharField(max_length=200, db_index=True)
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    slug = models.SlugField(max_length=100)
    file = models.FileField(upload_to=scheme_upload_to, blank=True)
    column_separator = models.CharField(max_length=50, choices=SEPARATOR, blank=False)
    string_character = models.CharField(max_length=50, choices=QUALIFIER, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('data-scheme', kwargs={'data_scheme': self.slug})


class Column(models.Model):
    TYPE = (
        ('full_name', 'Full name'),
        ('job', 'Job'),
        ('email', 'Email'),
        ('domain_name', 'Domain name'),
        ('phon_number', 'Phone number'),
        ('company_name', 'Company name'),
        ('text', 'Text'),
        ('integer', 'Integer'),
        ('address', 'Address'),
        ('date', 'Date'),
    )

    class Meta:
        verbose_name = "Column"
        verbose_name_plural = "Columns"
        ordering = ["name"]

    name = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=100, choices=TYPE, blank=False)
    data_scheme = models.ForeignKey(DataScheme, null=False, on_delete=models.CASCADE)
    order = models.IntegerField(null=False, default=0)
    range_from = models.IntegerField(null=True, blank=True)
    range_to = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
