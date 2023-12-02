from django.contrib import admin

from friendlists.models import FriendList, FriendRequest

# Register your models here.

class FriendListAdmin(admin.ModelAdmin):
    list_display = ('user',)
    
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('to_user', 'from_user')
    
admin.site.register(FriendList, FriendListAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)

