# Generated by Django 3.1.1 on 2020-10-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_runs', '0003_auto_20201006_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='duration',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='split',
            name='avg_pace',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='split',
            name='elapsed_time',
            field=models.FloatField(max_length=200),
        ),
        migrations.AlterField(
            model_name='split',
            name='moving_time',
            field=models.FloatField(max_length=200),
        ),
    ]
