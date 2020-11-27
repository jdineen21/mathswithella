from django.contrib import admin

from .models import Worksheet
from .models import WorksheetQuestion
#from .models import QuestionTemplate

class WorksheetQuestionInline(admin.TabularInline):
    model = WorksheetQuestion
    extra = 0
    ordering = ('number',)

class WorksheetAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'internal_name']
    ordering = ('display_name',)

    inlines = [
        WorksheetQuestionInline,
    ]

admin.site.register(Worksheet, WorksheetAdmin)
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(QuestionTemplate, QuestionTemplateAdmin)
