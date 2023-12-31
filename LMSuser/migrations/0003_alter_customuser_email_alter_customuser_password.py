# Generated by Django 4.2.5 on 2023-11-01 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSuser', '0002_customuser_is_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
