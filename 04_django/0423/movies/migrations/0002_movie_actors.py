# Generated by Django 3.2.7 on 2022-04-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor'),
        ),
    ]
