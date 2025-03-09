from django.db import models


class Medicine(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(max_length=255)
    img = models.URLField(max_length=255, blank=True, default='')
    manufacturer = models.CharField(max_length=255, blank=True, default='-')
    pharmacy = models.CharField(max_length=255)
    active_ingredient = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
