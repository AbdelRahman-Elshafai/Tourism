from django.db import models
from Countries.models import Cities
from Profile.models import Users
# Create your models here.


# table containing all hotel names and their id
class Hotel(models.Model):
    city_id = models.ForeignKey(Cities)
    hotel_name = models.CharField(max_length=200)
    hotel_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.hotel_name

# table linking user to hotels
class HotelReservationRequest(models.Model):
    hotel_id = models.ForeignKey(Hotel)
    user_id = models.ForeignKey(Users)
    from_date = models.DateField()
    to_date = models.DateField()
    no_of_adults = models.IntegerField()

