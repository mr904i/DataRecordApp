# Generated by Django 3.0 on 2019-12-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitbit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoursteps',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
