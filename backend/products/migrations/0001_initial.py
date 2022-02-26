# Generated by Django 4.0.2 on 2022-02-18 18:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=512)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]