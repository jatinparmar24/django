# Generated by Django 5.2 on 2025-05-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_students_stuimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('shop', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('color', models.CharField()),
            ],
        ),
    ]
