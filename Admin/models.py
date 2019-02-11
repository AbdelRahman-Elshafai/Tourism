from django.db import models

# Create your models here.


class Admin(models.Model):
    admin_username = models.CharField(max_length=200)
    admin_password = models.CharField(max_length=200)

    def __str__(self):
        return self.admin_username