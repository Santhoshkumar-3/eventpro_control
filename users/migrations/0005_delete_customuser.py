# Generated by Django 5.0.4 on 2024-04-27 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
