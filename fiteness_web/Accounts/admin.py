from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in CustomUser._meta.fields]
    list_display = ["email","first_name","last_name","date_joined","is_active","is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)
