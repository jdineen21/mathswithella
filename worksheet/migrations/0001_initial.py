# Generated by Django 3.1.2 on 2020-11-29 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=30)),
                ('internal_name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Worksheet',
                'verbose_name_plural': 'Worksheets',
            },
        ),
        migrations.CreateModel(
            name='WorksheetPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('worksheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worksheet.worksheet')),
            ],
            options={
                'verbose_name': 'Worksheet Page',
                'verbose_name_plural': 'Worksheet Pages',
            },
        ),
        migrations.CreateModel(
            name='WorksheetPageQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('question_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.questiontemplate')),
                ('worksheet_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worksheet.worksheetpage')),
            ],
            options={
                'verbose_name': 'Worksheet Page Question',
                'verbose_name_plural': 'Worksheets Page Questions',
            },
        ),
    ]
