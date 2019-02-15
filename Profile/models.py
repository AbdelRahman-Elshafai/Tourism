from django.db import models

# Create your models here.



class User(models.Model):
    # models.ForeignKey(User, on_delete=models.CASCADE) =>>> IN OTHER TABELS
    # A foreign key with cascade delete means that if a record in the parent table is deleted

    user_id     = models.AutoField(primary_key=True)
    user_name   = models.CharField(max_length=200)
    first_name  = models.CharField(max_length=200)
    last_name   = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email  = models.EmailField(max_length=200)
    blk_flg = models.BooleanField(default= False)



    def __int__(self):
        return self.user_id


    def __str__(self):
        return self.user_name
        return self.first_name
        return self.last_name
        return self.user_password
        return self.user_email

    def __bool__(self):
        return self.blk_flg





