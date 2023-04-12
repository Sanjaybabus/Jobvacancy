from django.db import models


# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.city_name}"

class Company(models.Model):
    Name = models.CharField(max_length = 50)
    jobdescription= models.CharField(max_length = 50)
    City = models.ForeignKey(City,on_delete=models.CASCADE)
    vacancy = models.IntegerField()
    applied = models.IntegerField()

