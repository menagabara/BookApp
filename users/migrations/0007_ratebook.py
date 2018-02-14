# Generated by Django 2.0.2 on 2018-02-13 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
        ('users', '0006_remove_favourite_books_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(1, 'very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'very Good'), (5, 'Excellent')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
