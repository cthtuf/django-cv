from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from contentful.cda.client import Client
from .models import *

# Create your views here.
def index(request):
	cfClient = Client(
		'82mi4zooxljq',
		'7f86a46952bf2432efe06a21ed02a3d481ec0924566ff1bd11be04822d936b12',
		custom_entries= [
			MainSlider,
			AboutMe,
			Awards,
			CommonSettings,
			Education,
			Portfolio,
			Process,
			Service,
			Skill,
			Testimonials,
			WorkExperience
		]
	)
	mainSlider = cfClient.fetch(MainSlider).all()
	aboutMe = cfClient.fetch(AboutMe).first()
	awards = cfClient.fetch(Awards).all()
	commonSettings = cfClient.fetch(CommonSettings).first()
	education = cfClient.fetch(Education).all()
	portfolio = cfClient.fetch(Portfolio).all()
	process = cfClient.fetch(Process).all()
	service = cfClient.fetch(Service).all()
	skill = cfClient.fetch(Skill).all()
	testimonials = cfClient.fetch(Testimonials).all()
	workExperience = cfClient.fetch(WorkExperience).all()

	template = loader.get_template('main/index.html')
	context = RequestContext(request, {
		'mainSlider' : mainSlider,
		'aboutMe' : aboutMe,
		'awards' : awards,
		'commonSettings' : commonSettings,
		'education' : education,
		'portfolio' : portfolio,
		'process' : process,
		'service' : service,
		'skill' : skill,
		'testimonials' : testimonials,
		'workExperience' : workExperience,
		}
	)
	return HttpResponse(template.render(context))

def feedback(request):
	return '{ success : 1 }'