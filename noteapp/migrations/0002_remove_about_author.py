# Generated by Django 5.0.3 on 2024-06-17 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='author',
        ),
    ]
