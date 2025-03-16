# Generated by Django 5.1.6 on 2025-03-14 03:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('salary', models.CharField(max_length=255)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.category')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=255)),
                ('candidate_email', models.EmailField(max_length=255)),
                ('resume_url', models.URLField(max_length=2000)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.job')),
            ],
        ),
    ]
