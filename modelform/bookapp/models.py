from django.db import models
class Booklet(models.Model):
    book = models.CharField(max_length=100,)
    author = models.CharField(max_length=50)