from django.contrib import admin

# Register your models here.



from .models import Admin


class CustomAdmin(admin.ModelAdmin):

    fieldsets = (
        ['Admin' , {'fields': ['admin_username' , 'admin_password']}],


    )



admin.site.register(Admin , CustomAdmin)