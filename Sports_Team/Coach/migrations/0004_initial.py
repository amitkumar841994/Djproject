# Generated by Django 4.1.1 on 2022-11-19 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Coach', '0003_delete_coach_register'),
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
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
