from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import *

@cache_page(60)
def index(request):
    slider_block = MainSliderBlock.objects.first()
    awards_block = AwardsBlock.objects.first()
    education_block = EducationBlock.objects.first()
    portfolio_block = PortfolioBlock.objects.first()
    process_block = ProcessBlock.objects.first()
    service_block = ServiceBlock.objects.first()
    skill_block = SkillBlock.objects.first()
    testimonials_block = TestimonialsBlock.objects.first()
    work_experience_block = WorkExperienceBlock.objects.first()
    video_block = VideoBlock.objects.filter()
    portfolio_types = PortfolioType.objects.all()
    get_in_touch_block = GetInTouchBlock.objects.first()
    cv_block = CVBlock.objects.first()
    about_me_block = AboutMeBlock.objects.first()
    settings = Settings.objects.all()
    seo = SEO.objects.first()

    context = {
        'slider_block': slider_block,
        'awards_block': awards_block,
        'education_block': education_block,
        'portfolio_block': portfolio_block,
        'portfolio_types': portfolio_types,
        'service_block': service_block,
        'process_block': process_block,
        'skill_block': skill_block,
        'video_block': video_block,
        'testimonials_block': testimonials_block,
        'work_experience_block': work_experience_block,
        'get_in_touch_block': get_in_touch_block,
        'cv_block': cv_block,
        'about_me_block': about_me_block,
        'seo': seo,
        'settings': settings,
    }
    return render(request, 'main/index.html', context)


def feedback(request):
    return '{ success : 1 }'
