from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff', 'date_joined', 'last_login')

    fieldsets   = ( 
            (None,{"fields":("username","email","password")}),
            (_("Personal info"),{"fields":("user_name","user_birthday","user_bithday_month","user_bithday_day","user_gender","user_address")}),
            (_("Permissions"),{"fields":("is_active","is_staff","is_superuser","groups","user_permissions")}),
            (_("Important dates"),{"fields":("last_login","date_joined")}),
    )   


admin.site.register(CustomUser, CustomUserAdmin)