# Generated by Django 4.2.2 on 2023-06-20 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_subscripe_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscripe',
            name='club',
        ),
        migrations.RemoveField(
            model_name='subscripe',
            name='user',
        ),
    ]
