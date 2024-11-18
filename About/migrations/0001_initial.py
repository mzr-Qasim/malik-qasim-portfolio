# Generated by Django 5.0.6 on 2024-11-09 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.CharField(blank=True, max_length=150, null=True)),
                ('introduction_description', models.CharField(blank=True, max_length=400, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(99)])),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'About Section',
            },
        ),
    ]
