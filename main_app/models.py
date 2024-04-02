from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=20)
    purpose = models.CharField(max_length=40)
    yearReleased = models.IntegerField()

    def __str__(self):
        return self.name