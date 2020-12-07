from django.contrib import admin

from worksheet.admin import WorksheetPageQuestionInline

from .models import QuestionTemplate

### Admin Pages ###

class QuestionTemplateAdmin(admin.ModelAdmin):
    list_display = [
        'display_name',
        'marks',
        'internal_name',
        'template_name',
        'created_at',
        'updated_at',
    ]

    inlines = [
        WorksheetPageQuestionInline,
    ]

### Admin Registrations ###

admin.site.register(QuestionTemplate, QuestionTemplateAdmin)