# Generated by Django 4.0.4 on 2022-05-06 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
