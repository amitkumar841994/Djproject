# Generated by Django 4.1.1 on 2022-11-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myfirstapp', '0007_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='gender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
