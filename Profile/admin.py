from django.contrib import admin
from .models import User
# register the models



class CustomModel(admin.ModelAdmin):
        fieldsets = (
        ['Users_Tabel' , {'fields': [ 'user_name' , 'first_name', 'last_name', 'user_password' , 'user_email']}],
        )
        list_display = ('user_id' ,'user_name' , 'first_name', 'last_name', 'user_password' , 'user_email' , 'blk_flg')


# Register your models here.
admin.site.register(User, CustomModel)