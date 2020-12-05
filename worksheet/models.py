import mathswithella.question

from django.db import models
from django.contrib.auth.models import User

from question.models import QuestionTemplate

class Worksheet(models.Model):
    display_name = models.CharField(max_length=30)
    internal_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.display_name)

    class Meta:
        verbose_name = 'Worksheet'
        verbose_name_plural = 'Worksheets'

class WorksheetPage(models.Model):
    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return '%s Page %s' % (self.worksheet, str(self.number))

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

class WorksheetPageQuestion(models.Model):
    worksheet_page = models.ForeignKey(WorksheetPage, on_delete=models.CASCADE)
    question_template = models.ForeignKey(QuestionTemplate, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return '%s Question %s' % (self.worksheet_page, str(self.number))

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
