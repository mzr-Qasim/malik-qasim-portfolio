# Generated by Django 5.0.6 on 2024-11-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=50, null=True)),
                ('title_details', models.TextField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Resume',
            },
        ),
    ]
