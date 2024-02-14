from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length = 255)
    Price = models.FloatField()
    Inventory = models.IntegerField(max_lenght=5)
        

class Booking(models.Model):
    Name = models.CharField(max_length = 255)
    No_of_guests = models.IntegerField(max_lenght = 6)
    BookingDate = models.DateTimeField()
    