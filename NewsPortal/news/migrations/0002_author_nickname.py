# Generated by Django 4.1.5 on 2023-01-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='nickname',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
