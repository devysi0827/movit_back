# Generated by Django 3.2.3 on 2021-05-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre_ids',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]