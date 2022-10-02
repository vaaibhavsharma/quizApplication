from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'ques_id', 'score']
    search_fields = ['user__username']