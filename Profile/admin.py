from django.contrib import admin
from .models import Users
# register the models



class customUser(admin.ModelAdmin):
    fieldsets = (
        ['User_info',{'fields':['password','last_login' , 'is_superuser' , 'username' , 'first_name' , 'last_name' , 'email' , 'is_staff' , 'is_active' , 'date_joined' , 'blk_flg']}],
    )


admin.site.register(Users, customUser)
