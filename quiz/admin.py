from django.contrib import admin
from .models import Question, inputQuestions
# Register your models here.
@admin.register(Question)
class inputQuestionsAdmin(admin.ModelAdmin):
    list_display = ['questionNumber', 'question', 'hint']
    search_fields = ['questionNumber']


@admin.register(inputQuestions)
class inputQuestionsAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'textAnswer', 'textTime', 'ipaddress']
    search_fields = ['user__username', 'textAnswer']

