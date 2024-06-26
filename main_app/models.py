from django.db import models
from datetime import date

# Create your models here.
TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)

class Sock(models.Model):
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.color

class Shoe(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=20)
    purpose = models.CharField(max_length=40)
    yearReleased = models.IntegerField()
    socks = models.ManyToManyField(Sock)

    def shoe_for_today(self):
        return self.wear_set.filter(date=date.today()).count() >= len(TIMES)
    
class Wear(models.Model):
    date = models.DateField('Wear Date')
    time = models.CharField(max_length=1, choices=TIMES, default=TIMES[0][0])

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.get_time_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']