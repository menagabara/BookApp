# Generated by Django 2.0.2 on 2018-02-13 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20180213_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(max_length=1000),
        ),
    ]
