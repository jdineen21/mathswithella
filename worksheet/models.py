import mathswithella.question

from django.db import models

from question.models import QuestionTemplate

class Worksheet(models.Model):
    display_name = models.CharField(max_length=30)
    internal_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.display_name)

    class Meta:
        verbose_name = 'Worksheet'
        verbose_name_plural = 'Worksheets'

class WorksheetQuestion(models.Model):
    number = models.IntegerField()
    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    question_template = models.ForeignKey(QuestionTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
