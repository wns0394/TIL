# Generated by Django 3.2.12 on 2022-04-14 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eithers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='either',
            old_name='blue',
            new_name='issue_a',
        ),
        migrations.RenameField(
            model_name='either',
            old_name='red',
            new_name='issue_b',
        ),
        migrations.RemoveField(
            model_name='either',
            name='blue_score',
        ),
        migrations.RemoveField(
            model_name='either',
            name='red_score',
        ),
    ]
