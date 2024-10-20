from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CarType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    car_type = models.ForeignKey(CarType, related_name='vehicles', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=10)
    instock = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)  # Optional field

    def __str__(self):
        return self.car_name

class Buyer(User):
    AREA_CHOICES = [
        ('C', 'Chatham'),
        ('W', 'Windsor'),
        ('LS', 'LaSalle'),
        ('A', 'Amherstburg'),
        ('L', 'Lakeshore'),
        ('LE', 'Leamington'),
    ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='C')
    interested_in = models.ManyToManyField(CarType)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username


class OrderVehicle(models.Model):
    STATUS_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Placed'),
        (2, 'Shipped'),
        (3, 'Delivered'),
    ]
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.buyer.username}"

    def total_price(self):
        return self.quantity * self.vehicle.car_price



class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    semester = models.IntegerField()
    personal_link = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['first_name']
