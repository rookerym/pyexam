# Generated by Django 2.2 on 2020-11-19 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exapp', '0002_quote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='content',
            new_name='quote',
        ),
    ]