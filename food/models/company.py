from django.db import models
from django.contrib import admin
from .category import Category

class Company(models.Model):
    logo = models.FileField(upload_to='uploads/',null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    desconto = models.IntegerField(null=True, blank=True)
    mon = models.BooleanField(default=True)
    mon_open = models.CharField(max_length=20, null=True, blank=True)
    mon_close = models.CharField(max_length=20, null=True, blank=True)

    tue = models.BooleanField(default=True)
    tue_open = models.CharField(max_length=20, null=True, blank=True)
    tue_close = models.CharField(max_length=20, null=True, blank=True)

    wed = models.BooleanField(default=True)
    wed_open = models.CharField(max_length=20, null=True, blank=True)
    wed_close = models.CharField(max_length=20, null=True, blank=True)

    thu = models.BooleanField(default=True)
    thu_open = models.CharField(max_length=20, null=True, blank=True)
    thu_close = models.CharField(max_length=20, null=True, blank=True)

    fri = models.BooleanField(default=True)
    fri_open = models.CharField(max_length=20, null=True, blank=True)
    fri_close = models.CharField(max_length=20, null=True, blank=True)

    sat = models.BooleanField(default=True)
    sat_open = models.CharField(max_length=20, null=True, blank=True)
    sat_close = models.CharField(max_length=20, null=True, blank=True)

    sun = models.BooleanField(default=True)
    sun_open = models.CharField(max_length=20, null=True, blank=True)
    sun_close = models.CharField(max_length=20, null=True, blank=True)

    # Slides
    photo1 = models.FileField(upload_to='uploads/', null=True, blank=True)
    photo2 = models.FileField(upload_to='uploads/', null=True, blank=True)
    photo3 = models.FileField(upload_to='uploads/', null=True, blank=True)
    photo4 = models.FileField(upload_to='uploads/', null=True, blank=True)
    photo5 = models.FileField(upload_to='uploads/', null=True, blank=True)

    # Localizacao
    localizacao = models.TextField(null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    lng = models.CharField(max_length=255, null=True, blank=True)

    # Relacoes
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    photo_yelp = models.TextField(null=True, blank=True)
    rating_yelp = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

