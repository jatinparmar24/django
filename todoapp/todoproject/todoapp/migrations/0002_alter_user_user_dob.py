# Generated by Django 5.2.1 on 2025-06-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_dob',
            field=models.DateField(),
        ),
    ]
