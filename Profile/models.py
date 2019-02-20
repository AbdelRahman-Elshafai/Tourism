from django.db import models

from django.contrib.auth.models import User, AbstractUser

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Users(models.Model):
#     # models.ForeignKey(User, on_delete=models.CASCADE) =>>> IN OTHER TABELS
#     # A foreign key with cascade delete means that if a record in the parent table is deleted
#
#     # user_id     = models.AutoField(primary_key=True )
#     user = models.OneToOneField(User , on_delete=models.CASCADE)
#     username   = models.CharField(max_length=200 ,  unique=True)
#     first_name  = models.CharField(max_length=200)
#     last_name   = models.CharField(max_length=200)
#     user_password = models.CharField(max_length=200)
#     user_email  = models.EmailField(max_length=200 )
#     blk_flg = models.BooleanField(default= False)
#
#     def __int__(self):
#         return self.user_id
#
#     def __str__(self):
#         return self.username
#         return self.first_name
#         return self.last_name
#         return self.user_password
#         return self.user_email
#
#     def __bool__(self):
#         return self.blk_flg
#
#
# # when u save user.auth save in your table the same values
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         print(instance)
#         Users.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.users.save()



class Users(AbstractUser):
    blk_flg = models.BooleanField(default=False)




