'''
 in this class, there are few assumptions assumed in designing table "Car_Rental".
 #1 -> name of table that car_Rental references is "Location".
 #2 -> the foreign key is assumed to be of type CharField (although this is not an issue).
'''

from django.db        import models

from Profile.models   import Users
from Countries.models import Locations

from django.conf import settings

# Create your models here.
#class representing table for car rentals services
# class Car_Rental (models.Model):
#
#
#     # setting fields of the table
#     car_rental_id = models.AutoField(primary_key=True)
#     car_rental_name = models.CharField(max_length=45)
#     location_ID = models.ForeignKey(Locations , null=True)
#
#     def __str__(self):
#         return self.car_rental_name

class Car_Reservation(models.Model):

    reservation_id = models.AutoField(primary_key=True )
    location_ID = models.ForeignKey(Locations , null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    pick_up = models.CharField(max_length = 200 , null=True)
    drop_off = models.CharField(max_length = 200 , null=True)
    def __str__(self):
        return self.reservation_id
