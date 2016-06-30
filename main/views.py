from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from contentful.cda.client import Client
from .models import *
from pprint import pprint as print

def order_by_index(obj):
    '''
    Hardcoded sort method based on the field 'index' in my content models in Contentful.
    Used because of contentful.py doesn't have it
    '''

    return sorted(obj, key=lambda o: o.index)

# Create your views here.
def index(request):
    cfClient = Client(
        '82mi4zooxljq',
        '7f86a46952bf2432efe06a21ed02a3d481ec0924566ff1bd11be04822d936b12',
        custom_entries= [
            MainSlider,
            Awards,
            CommonData,
            Education,
            Portfolio,
            Process,
            Service,
            Skill,
            Testimonials,
            WorkExperience,
        ]
    )
    mainSlider = cfClient.fetch(MainSlider).all()
    awards = order_by_index(cfClient.fetch(Awards).all())
    commonData = cfClient.fetch(CommonData).first()
    education = order_by_index(cfClient.fetch(Education).all())
    portfolio = order_by_index(cfClient.fetch(Portfolio).all())
    process = order_by_index(cfClient.fetch(Process).all())
    service = order_by_index(cfClient.fetch(Service).all())
    skill = order_by_index(cfClient.fetch(Skill).all())
    testimonials = order_by_index(cfClient.fetch(Testimonials).all())
    workExperience = order_by_index(cfClient.fetch(WorkExperience).all())

    print(portfolio[0].portfolioType)

    template = loader.get_template('main/index.html')
    context = RequestContext(request, {
      'mainSlider' : mainSlider,
      'awards' : awards,
      'commonData' : commonData,
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
