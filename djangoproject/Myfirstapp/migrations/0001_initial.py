# Generated by Django 4.1.1 on 2022-10-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Food_id', models.IntegerField()),
                ('Food_name', models.CharField(max_length=50)),
                ('Food_price', models.IntegerField()),
                ('Food_cate', models.CharField(max_length=50)),
            ],
        ),
    ]
