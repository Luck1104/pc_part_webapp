# Generated by Django 5.0.4 on 2024-05-03 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cpu',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='gpu',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='ram',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='storage',
            options={'ordering': ['-name']},
        ),
    ]