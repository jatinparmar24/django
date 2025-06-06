# Generated by Django 5.2 on 2025-04-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=50)),
                ('stuemial', models.EmailField(max_length=254)),
                ('studetails', models.CharField(max_length=200)),
                ('stuphone', models.IntegerField()),
                ('studob', models.DateField()),
                ('stuedu', models.CharField(max_length=50)),
                ('stugender', models.CharField(max_length=50)),
                ('stuimage', models.ImageField(upload_to='image/')),
                ('sturesume', models.FileField(upload_to='file/')),
                ('stupass', models.CharField(max_length=50)),
            ],
        ),
    ]
