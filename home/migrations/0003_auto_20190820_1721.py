# Generated by Django 2.2.3 on 2019-08-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190820_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='exercise',
            field=models.CharField(choices=[('pullup', 'pullup'), ('pushup', 'pushup'), ('squat', 'squat')], default='pullup', max_length=100),
        ),
    ]
