from django.db import models
class local(models.Model):
    title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    year = models.CharField(max_length=100)

