# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Resturent

from django.views import generic
from django.views.generic.list import ListView

from .forms import ResturentSearchForm

#from search_views.search import SearchListView

from django.contrib.auth.mixins import LoginRequiredMixin

class ResturentSearchList(LoginRequiredMixin, ListView):
	login_url = '/login/'
	model = Resturent
	paginate_by = 10
	template_name= 'resturent/resturant_list.html'
	form_class = ResturentSearchForm

	def get_queryset(self):
		form = self.form_class(self.request.GET)
		
		if 'location' in form.data and form.data['location']:
			print(form.data) 						
			queryset = Resturent.objects.all().order_by('name')[0:10]
			return queryset
		else:
			queryset = Resturent.objects.all()[0:100]
			return queryset

