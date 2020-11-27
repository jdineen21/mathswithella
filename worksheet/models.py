import mathswithella.question

from django.db import models

from inspect import getmembers, isfunction

class Worksheet(models.Model):
    display_name = models.CharField(max_length=30)
    internal_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.display_name)

    class Meta:
        verbose_name = 'Worksheet'
        verbose_name_plural = 'Worksheets'

class QuestionTemplate(models.Model):
    display_name = models.CharField(max_length=50)
    internal_name = models.CharField(max_length=50)
    template_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.display_name)

    class Meta:
        verbose_name = 'Question Template'
        verbose_name_plural = 'Question Templates'

class Question(models.Model):
    number = models.IntegerField()
    worksheet = models.ForeignKey(Worksheet, on_delete=models.CASCADE)
    question_template = models.ForeignKey(QuestionTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
