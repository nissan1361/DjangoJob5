from django.contrib import admin
from .models import *


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title']}
         ),
        ('Информация о дате',
         {'fields': ['date_published'],
          'classes': ['collapse']}
         ),
    ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)



admin.site.register(QuestionText)
admin.site.register(Text)
