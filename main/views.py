from django.shortcuts import render
from django.http import HttpResponse
from contentful.cda.client import *
from main.models import *

# Create your views here.
def index(request):
	cfClient = Client('82mi4zooxljq', '7f86a46952bf2432efe06a21ed02a3d481ec0924566ff1bd11be04822d936b12', custom_entries=[MainSlider])
	sliderRecord = cfClient.fetch(MainSlider).first()
	return HttpResponse(sliderRecord.header)