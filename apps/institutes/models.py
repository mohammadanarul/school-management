from django.db import models
from apps.helpers.models import BaseEntity


class Institute(BaseEntity):
    name = models.CharField(max_length=255)
    established_year = models.SmallIntegerField()
    president = models.CharField()
    principal = models.CharField(max_length=255)
    website_domain_address = models.URLField()
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number_1 = models.CharField(max_length=14)
    phone_number_2 = models.CharField(max_length=14)
    image = models.ImageField(upload_to='institute-images/')
    logo = models.ImageField(upload_to='institute-logo-images/')
    eiin_number = models.CharField(max_length=100)
    institute_code = models.CharField(max_length=100)
    institute_type = models.SmallIntegerField()
    institute_abouts = models.TextField()
