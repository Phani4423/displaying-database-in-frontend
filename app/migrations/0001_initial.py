# Generated by Django 5.0.7 on 2024-09-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='topics',
            fields=[
                ('topic_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
