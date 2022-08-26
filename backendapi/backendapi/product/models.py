from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    valuation = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)