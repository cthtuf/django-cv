from django.db import models
from contentful.cda.fields import *
from contentful.cda.resources import *

# Create your models here.
class MainSlider(Entry):
	__content_type__ = 'mainSlider'

	imageLink = Field(Text)
	header = Field(Text)
	subHeader = Field(Text)
	slogan = Field(Text)