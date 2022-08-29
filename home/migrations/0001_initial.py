# Generated by Django 4.1 on 2022-08-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='changes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sportsname', models.TextField(default=None)),
                ('capacity', models.IntegerField()),
                ('inventory', models.CharField(max_length=250)),
                ('slots', models.IntegerField()),
                ('courts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=100)),
                ('bookedfor', models.TextField(default=None)),
            ],
        ),
    ]
