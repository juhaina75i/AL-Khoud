# Generated by Django 4.2.2 on 2023-06-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_delete_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate ', 'Intermediate '), ('Advanced', 'Advanced')], max_length=128),
        ),
    ]