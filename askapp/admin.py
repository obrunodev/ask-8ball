from django.contrib import admin

from .models import Answer, Question


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'answer', 'created')
