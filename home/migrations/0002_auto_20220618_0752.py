# Generated by Django 3.2.5 on 2022-06-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='image_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='question_id',
            field=models.IntegerField(),
        ),
    ]