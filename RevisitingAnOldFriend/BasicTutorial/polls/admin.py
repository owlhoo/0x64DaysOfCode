# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice


# class ChoiceInLine(admin.StackedInline):
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question',         {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


# Choice in line replaces this I guess xd
# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Choice',          {'fields': ['choice_text']}),
#         ('Votes',           {'fields': ['votes']}),
#         ('Question source', {'fields': ['question']})
#     ]
# admin.site.register(Choice, ChoiceAdmin)


admin.site.register(Question, QuestionAdmin)

