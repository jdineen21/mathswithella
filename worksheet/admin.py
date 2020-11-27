from django.contrib import admin

from .models import Worksheet
from .models import Question
from .models import QuestionTemplate

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    ordering = ('number',)

class WorksheetAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'internal_name']
    ordering = ('display_name',)

    inlines = [
        QuestionInline,
    ]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['worksheet', 'number', 'question_template']
    change_list_template = 'worksheet/admin/change_list.html'
    ordering = ('worksheet', 'number')

class QuestionTemplateAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'internal_name', 'template_name']

admin.site.register(Worksheet, WorksheetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionTemplate, QuestionTemplateAdmin)
