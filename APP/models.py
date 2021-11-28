from django.db import models
from django.contrib import admin
from django.conf import settings

class FB(models.Model):
	name = models.TextField(verbose_name="Имя")
	phone = models.CharField(verbose_name="Номер телефона", max_length=16)

class Meta:
	verbose_name = "Заявка"
	verbose_name_plural = "Заявки"

def __str__(self):
	return self.phone

class Articles(models.Model):
	photo = models.ImageField(upload_to='C:/django/hello/APP/static/img/товары', blank=True)
	title = models.CharField('Название', max_length=30)
	price = models.CharField('Цена', max_length=10)	

def __str__(self):
	return self.title