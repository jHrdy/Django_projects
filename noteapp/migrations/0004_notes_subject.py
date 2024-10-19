# Generated by Django 5.0.3 on 2024-06-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_remove_about_title_notes_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='subject',
            field=models.CharField(choices=[('maths', 'Maths'), ('physics', 'Physics'), ('programming', 'Programming'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]