# Generated by Django 3.1.2 on 2020-11-26 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worksheet', '0003_auto_20201126_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_name', models.CharField(max_length=50)),
                ('template_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Question Template',
                'verbose_name_plural': 'Question Templates',
            },
        ),
        migrations.RemoveField(
            model_name='question',
            name='internal_name',
        ),
        migrations.RemoveField(
            model_name='question',
            name='template_name',
        ),
        migrations.AlterField(
            model_name='question',
            name='num',
            field=models.IntegerField(unique=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='worksheet.questiontemplate'),
            preserve_default=False,
        ),
    ]
