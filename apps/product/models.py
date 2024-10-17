from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    next_state = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, models.CASCADE)
    next_state = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    def file_path(self):
        return f"products/demo_files/{self.code}"

    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    file = models.FileField(upload_to=file_path)

    def __str__(self):
        return self.name
