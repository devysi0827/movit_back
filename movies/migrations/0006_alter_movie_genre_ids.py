# Generated by Django 3.2.3 on 2021-05-20 18:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_genre_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), default=1, size=None),
            preserve_default=False,
        ),
    ]