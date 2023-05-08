from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)


class Middlewares(models.Model):
    path = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
