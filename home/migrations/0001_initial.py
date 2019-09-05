# Generated by Django 2.2.3 on 2019-08-19 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(default='pullup', max_length=100)),
                ('points', models.PositiveIntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
