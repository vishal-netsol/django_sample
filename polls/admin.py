from django.contrib import admin

# Register your models here.

from .models import *

class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(UserDetail)

admin.site.register(Choice)

admin.site.register(Contact)

admin.site.register(User)


