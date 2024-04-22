from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('payload', 'users', "Like_Count",'created_at', 'updated_at')
    search_fields = ('payload', 'users__name')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'user', 'created_at', 'updated_at')
    search_fields = ('tweet__payload', 'user__name')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)