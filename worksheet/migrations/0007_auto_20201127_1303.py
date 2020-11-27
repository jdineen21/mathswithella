# Generated by Django 3.1.2 on 2020-11-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksheet', '0006_auto_20201126_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='display_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='internal_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='template_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='QuestionTemplate',
        ),
    ]