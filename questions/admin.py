from django.contrib import admin
from .models import Questions,Answers
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answers

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ AnswerInline]

admin.site.register(Questions,QuestionAdmin)
admin.site.register(Answers)