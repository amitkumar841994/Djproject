# Generated by Django 4.1.1 on 2022-11-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('Dob', models.DateField()),
                ('Address', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('Coach_for', models.CharField(max_length=100)),
                ('Experience', models.IntegerField()),
            ],
        ),
    ]
