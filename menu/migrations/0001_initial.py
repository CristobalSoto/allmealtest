# Generated by Django 5.1.1 on 2024-09-27 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('starter', models.CharField(max_length=255)),
                ('main_course', models.CharField(max_length=255)),
                ('dessert', models.CharField(max_length=255)),
            ],
        ),
    ]
