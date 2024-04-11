from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    titles = models.CharField(max_length=100)
    microchipnr = models.IntegerField()
    handler = models.CharField(max_length=100)

    def __str__(self):
        return self.name