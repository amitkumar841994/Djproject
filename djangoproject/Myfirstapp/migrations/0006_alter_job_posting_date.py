# Generated by Django 4.1.1 on 2022-11-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myfirstapp', '0005_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='posting_date',
            field=models.DateField(),
        ),
    ]