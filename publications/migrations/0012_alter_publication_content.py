# Generated by Django 3.2 on 2021-06-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0011_alter_publication_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='content',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]