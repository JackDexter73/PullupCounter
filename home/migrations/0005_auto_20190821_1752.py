# Generated by Django 2.2.3 on 2019-08-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190820_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='reps',
            field=models.PositiveIntegerField(default=0),
        ),
    ]