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


class SearchQuery(models.Model):
    MODE_TITLE = "title"
    MODE_INGREDIENT = "ingredient"
    MODE_CHOICES = [
        (MODE_TITLE, "title"),
        (MODE_INGREDIENT, "ingredient"),
    ]

    query = models.CharField(max_length=255)
    query_norm = models.CharField(max_length=255, db_index=True)
    mode = models.CharField(max_length=32, choices=MODE_CHOICES, default=MODE_TITLE, db_index=True)
    session_key = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=["mode", "query_norm", "-created_at"]),
            models.Index(fields=["session_key", "-created_at"]),
        ]

    def __str__(self):
        return f"{self.query} ({self.mode})"
