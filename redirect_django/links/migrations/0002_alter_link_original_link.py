# Generated by Django 4.0.2 on 2022-02-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='original_link',
            field=models.URLField(unique=True),
        ),
    ]
