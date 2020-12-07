from django.contrib import admin

from .models import Worksheet, WorksheetPage, WorksheetPageQuestion

### Inlines ###

class WorksheetPageInline(admin.TabularInline):
    model = WorksheetPage
    extra = 0

class WorksheetPageQuestionInline(admin.TabularInline):
    model = WorksheetPageQuestion
    extra = 0

### Admin Pages ###

class WorksheetAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'internal_name']
    ordering = ['display_name']

    inlines = [
        WorksheetPageInline,
    ]

class WorksheetPageAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    ordering = ['worksheet', 'number']

    inlines = [
        WorksheetPageQuestionInline,
    ]

class WorksheetPageQuestionAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    ordering = ['worksheet_page', 'number']

### Admin Registrations ###

admin.site.register(Worksheet, WorksheetAdmin)
admin.site.register(WorksheetPage, WorksheetPageAdmin)
admin.site.register(WorksheetPageQuestion, WorksheetPageQuestionAdmin)
