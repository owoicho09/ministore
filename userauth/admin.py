from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields =['full_name', 'username']
    list_display =['full_name', 'email', 'username']


admin.site.register(User, UserAdmin)