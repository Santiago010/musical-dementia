# Generated by Django 3.2 on 2021-05-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20210512_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=models.TextField(default='Contenido no especificado'),
        ),
    ]