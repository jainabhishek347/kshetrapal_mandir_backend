# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Resturent(models.Model):
	"""
	"""
	id = models.AutoField(primary_key=True)
	location_id = models.CharField(max_length=100, default='')	
	address = models.TextField(default='')
	categories = models.TextField(default='')
	primaryCategories = models.TextField(default='')
	city = models.CharField(max_length=100, default='')
	country = models.CharField(max_length=100, default='')
	keys = models.TextField(default='')
	latitude = models.CharField(max_length=100, default='')
	longitude = models.CharField(max_length=100, default='')
	name = models.CharField(max_length=100, default='')
	postalCode = models.CharField(max_length=100, default='')
	province = models.CharField(max_length=100, default='')
	sourceURLs = models.TextField(default='')
	websites = models.TextField(default='')
	
	def __str__(self):
		return self.name		


class UserLocation(models.Model):
	"""
	"""

	user_id = models.ForeignKey(User, on_delete=models.CASCADE)	
	fisrt_name = models.CharField(max_length=100, default='')
	address = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=50, default='')

	def __str__(self):
		return self.user_id		