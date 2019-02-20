from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class UserProfile(AbstractUser):

    blk_flg = models.BooleanField(default= False)




    def __bool__(self):
        return self.blk_flg





