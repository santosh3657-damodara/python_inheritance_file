# Generated by Django 5.1.3 on 2025-05-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('college', models.CharField(max_length=100)),
                ('gf', models.CharField(max_length=60)),
                ('bf', models.CharField(max_length=60)),
            ],
        ),
    ]
