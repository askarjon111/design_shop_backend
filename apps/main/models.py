from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=12)
    telegram_id = models.CharField(max_length=50, unique=True)
    company = models.CharField(max_length=250, blank=True, null=True)
    lang = models.CharField(max_length=2)

    def __str__(self):
        return self.name
