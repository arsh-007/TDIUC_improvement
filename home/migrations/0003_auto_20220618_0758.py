# Generated by Django 3.2.5 on 2022-06-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220618_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='image_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='initial_answer',
            field=models.TextField(default='init'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='question_id',
            field=models.IntegerField(default=1),
        ),
    ]
