# Generated by Django 4.0.4 on 2022-04-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spy', '0002_userprofile_complete_mission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='status',
            field=models.CharField(max_length=8),
        ),
    ]
