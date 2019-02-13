from django.db import models
from Profile.models import User

# Create your models here.
class Countries(models.Model):
    country_ID=models.AutoField(primary_key=True)
    country_name=models.CharField(max_length=50)
    local_name=models.CharField(max_length=3)
    latitude=models.FloatField()
    longitude=models.FloatField()
    def __str__(self):
        return self.country_ID


class Cities(models.Model):
    city_ID = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)
    local_name = models.CharField(max_length=3)
    country_ID = models.ForeignKey(Countries)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description=models.TextField()

class locations(models.Model):
    location_ID = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    city_ID = models.ForeignKey(Cities)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()



class Experience(models.Model):
    exper_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(User)
    city_ID = models.ForeignKey(Cities)
    date=models.DateTimeField()
    description = models.TextField()


class Comments(models.Model):
    comment_ID = models.AutoField(primary_key=True)
    user_ID = models.ForeignKey(User)
    exper_ID = models.ForeignKey(Experience)
    date = models.DateTimeField()
    description = models.TextField()