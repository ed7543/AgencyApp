from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    sales_number = models.IntegerField()
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,  blank=True)

    def __str__(self):
        return f"{self.name} - {self.surname}"

class Characteristic(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.value}"

class RealEstate(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    surface = models.FloatField()
    date = models.DateField()
    image = models.ImageField(upload_to='real_estates/')
    reserved = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    agent = models.ManyToManyField(Agent)
    characteristics = models.ManyToManyField(Characteristic)
    #id = models.AutoField(primary_key=True) #za edit forma

    def __str__(self):
        return f"{self.name} - {self.location}"




