from django.contrib import admin
from .models import Choice, GrammarQuestions

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class GrammarQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question text:',{'fields':['text']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(GrammarQuestions, GrammarQuestionAdmin)
