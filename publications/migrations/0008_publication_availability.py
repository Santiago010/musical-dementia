# Generated by Django 3.2 on 2021-06-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0007_auto_20210514_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='availability',
            field=models.BooleanField(default=False),
        ),
    ]
