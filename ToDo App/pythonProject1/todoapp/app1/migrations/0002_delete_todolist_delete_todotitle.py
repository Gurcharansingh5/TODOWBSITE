# Generated by Django 4.0.6 on 2022-07-14 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='todolist',
        ),
        migrations.DeleteModel(
            name='todotitle',
        ),
    ]
