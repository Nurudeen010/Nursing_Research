# Generated by Django 5.0.1 on 2024-01-29 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_alter_researchmodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchmodel',
            name='id',
            field=models.IntegerField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
