from django.db import models
from contentful.cda.fields import *
from contentful.cda.resources import *

# Create your models here.
class MainSlider(Entry):
	__content_type__ = 'mainSlider'

	index = Field(Number)
	image = Field(Link)
	header = Field(Text)
	subHeader = Field(Text)
	slogan = Field(Text)

class AboutMe(Entry):
	__content_type__ = 'aboutMe'

	fullName = Field(Text)
	birthday = Field(Text)
	birthPlace = Field(Text)
	hobbies = Field(Text)
	photos = Field(Link)
	address = Field(Text)
	phone = Field(Text)
	email = Field(Text)
	website = Field(Text)
	shortInfo = Field(Text)
	longInfo = Field(Text)

class Awards(Entry):
	__content_type__ = 'awards'

	index = Field(Number)
	title = Field(Text)
	companyName = Field(Text)
	date = Field(Text)
	image = Field(Link)

class CommonSettings(Entry):
	__content_type__ = 'commonSettings'

	descriptionSkills = Field(Text)
	descriptionEducation = Field(Text)
	descriptionProcess = Field(Text)
	descriptionWorkExperience = Field(Text)
	descriptionServices = Field(Text)
	descriptionPortfolio = Field(Text)
	descriptionAwards = Field(Text)
	descriptionDownloadCv = Field(Text)
	descriptionGetInTouch = Field(Text)
	video = Field(Link)
	contactAddress = Field(Text)
	contactPhone = Field(Text)
	contactEmail = Field(Text)
	contactWebsite = Field(Text)
	socialFacebook = Field(Text)
	socialLinkedIn = Field(Text)
	socialVk = Field(Text)
	socialGooglePlus = Field(Text)

class Education(Entry):
	__content_type__ = 'education'

	index =  Field(Number)
	grade = Field(Text)
	universityName = Field(Text)
	country = Field(Text)
	datePeriod = Field(Text)
	description = Field(Text)

class Portfolio(Entry):
	__content_type__ = 'portfolio'

	index = Field(Number)
	header = Field(Text)
	subHeader = Field(Text)
	image = Field(Link)

class Process(Entry):
	__content_type__ = 'process'

	index = Field(Number)
	name = Field(Text)
	icon = Field(Text)

class Service(Entry):
	__content_type__ = 'service'

	index = Field(Number)
	name = Field(Text)
	description = Field(Text)
	icon = Field(Text)

class Skill(Entry):
	__content_type__ = 'skill'

	index = Field(Number)
	name = Field(Text)
	persent = Field(Number)

class Testimonials(Entry):
	__content_type__ = 'testimonials'

	index = Field(Number)
	name = Field(Text)
	companyName = Field(Text)
	text = Field(Text)

class WorkExperience(Entry):
	__content_type__ = 'workExperience'

	index = Field(Number)
	companyName = Field(Text)
	position = Field(Text)
	datePeriod = Field(Text)
	description = Field(Text)
	companyUrl = Field(Text)