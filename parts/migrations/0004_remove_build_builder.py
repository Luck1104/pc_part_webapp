# Generated by Django 5.0.2 on 2024-05-04 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_build'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='build',
            name='builder',
        ),
    ]
