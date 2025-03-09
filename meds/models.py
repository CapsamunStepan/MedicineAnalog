from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    active_ingredient = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pharmacy = models.CharField(max_length=255)

    def __str__(self):
        return self.name
