# Generated by Django 3.2 on 2021-10-31 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='C:/django/hello/APP/static/img/товары', blank=True, verbose_name='Название')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
            ],
        ),
    ]
