# Generated by Django 5.0.1 on 2024-01-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0002_researchmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchmodel',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='researchmodel',
            name='title',
            field=models.TextField(max_length=500),
        ),
    ]
