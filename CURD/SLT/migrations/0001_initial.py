# Generated by Django 5.0.3 on 2024-03-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=75)),
                ('Age', models.IntegerField()),
                ('Cource', models.CharField(max_length=75)),
            ],
        ),
    ]
