from django.contrib import admin
from .models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    ordering = ['create_date']
    search_fields=['subject']



admin.site.register(Question, QuestionAdmin)
