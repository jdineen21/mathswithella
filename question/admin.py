from django.contrib import admin

from .models import QuestionTemplate

class QuestionTemplateAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'marks', 'internal_name', 'template_name']

admin.site.register(QuestionTemplate, QuestionTemplateAdmin)