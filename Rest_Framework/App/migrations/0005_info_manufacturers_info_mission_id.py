# Generated by Django 4.1.1 on 2022-09-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_rename_name_info_mission_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='manufacturers',
            field=models.CharField(default='NaN', max_length=50),
        ),
        migrations.AddField(
            model_name='info',
            name='mission_id',
            field=models.CharField(default='NaN', max_length=10),
        ),
    ]
