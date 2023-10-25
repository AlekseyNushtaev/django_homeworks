from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.URLField(max_length=200)
    release_date = models.DateField(default=None)
    lte_exists = models.BooleanField(default=None)
    slug = models.SlugField(max_length=200)


