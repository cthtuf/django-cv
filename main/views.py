from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from contentful.cda.client import Client
from .models import MainSlider

# Create your views here.
def index(request):
	cfClient = Client('82mi4zooxljq', '7f86a46952bf2432efe06a21ed02a3d481ec0924566ff1bd11be04822d936b12', custom_entries=[MainSlider])
	sliderRecords = cfClient.fetch(MainSlider).all()
	template = loader.get_template('main/index.html')
	context = RequestContext(request, {
		'sliderRecords' : sliderRecords
		})
	return HttpResponse(template.render(context))