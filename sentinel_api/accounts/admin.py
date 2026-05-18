from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'role')
    list_editable = ('role',)
    search_fields = ('username', 'email', 'phone_number', 'role')
    fields = ('username', 'email', 'phone_number', 'profile_image', 'role', 'is_staff', 'is_active')

admin.site.register(User, UserAdmin)
