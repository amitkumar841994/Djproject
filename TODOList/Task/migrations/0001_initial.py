# Generated by Django 4.1.1 on 2022-11-10 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_name', models.CharField(max_length=100)),
                ('Task_status', models.CharField(default='In-progress', max_length=50)),
            ],
        ),
    ]