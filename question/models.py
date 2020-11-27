from django.db import models

class QuestionTemplate(models.Model):
    display_name = models.CharField(max_length=50)
    internal_name = models.CharField(max_length=50)
    template_name = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return str(self.display_name)

    class Meta:
        verbose_name = 'Question Template'
        verbose_name_plural = 'Question Templates'