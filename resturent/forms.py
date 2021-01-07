from .models import Resturent
from django import forms
from django.forms import ModelForm

class ResturentSearchForm(ModelForm):
	class Meta:
		model = Resturent
		fields = ['name']
		