# Generated by Django 4.2.2 on 2023-06-19 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='club',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.club'),
        ),
        migrations.AddField(
            model_name='package',
            name='club',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.club'),
        ),
    ]
