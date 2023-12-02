from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'display_name', 'date_joined')
    list_filter = ('is_active', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'display_name', 'bio') 
    readonly_fields = ('date_joined',)
    filter_horizontal = ()
    list_per_page = 25
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'display_name', 'bio', 'profile_pic', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser')}),
    )
    
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'display_name', 'bio', 'profile_pic', 'date_joined', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser')}),
    )
    
    ordering = ('-date_joined',)
    
admin.site.register(CustomUser, CustomUserAdmin)
