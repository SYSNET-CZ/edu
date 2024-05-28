# Generated by Django 4.2.13 on 2024-05-24 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=256)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=64)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('amount', models.IntegerField(default=1)),
                ('total', models.FloatField(default=0.0, null=True)),
                ('ticket', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cestovani.ticket')),
            ],
        ),
    ]
