# Generated by Django 5.0.1 on 2024-01-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0007_alter_researchmodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='class_level',
            field=models.CharField(choices=[('Year_one', 'Year One'), ('Year_two', 'Year Two'), ('Year_three', 'Year Three'), ('other', 'Other')], default='Year_one', max_length=50),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='name_of_school',
            field=models.CharField(max_length=50),
        ),
    ]
