from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'role')
    search_fields = ('username', 'email', 'phone_number', 'role')
