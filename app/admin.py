from django.contrib import admin
from .models import MyUser, Gift

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('gift_name', 'user')
    search_fields = ('gift_name',)
    list_filter = ('user',)
