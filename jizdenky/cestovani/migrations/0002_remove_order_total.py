# Generated by Django 4.2.13 on 2024-05-29 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cestovani', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
