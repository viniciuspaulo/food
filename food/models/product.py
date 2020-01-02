from django.db import models
from .company import Company

class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    photo = models.CharField(max_length=255, null=True, blank=False)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
