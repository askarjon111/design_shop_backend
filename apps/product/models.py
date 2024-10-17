from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)


class Event(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, models.CASCADE)


class Product(models.Model):
    def file_path(self):
        return f"products/demo_files/{self.code}"

    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    file = models.FileField(upload_to=file_path)
