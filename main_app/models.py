from django.db import models
from django.urls import reverse

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=150)
  date = models.DateField('Event Date')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('events_detail', kwargs={'pk': self.id})

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    titles = models.CharField(max_length=100)
    microchipnr = models.IntegerField()
    handler = models.CharField(max_length=100)
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id: self.id'})
    
class Trial(models.Model):
    date = models.DateField('Trial Date')
    name = models.CharField(max_length=100)
    judge = models.CharField(max_length=100)
    score = models.IntegerField()

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

