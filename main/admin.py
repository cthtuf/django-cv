from django.contrib import admin

from .models import (AboutMeBlock, AwardsBlock, AwardRecord, CVBlock,
                     EducationBlock, EducationRecord, GetInTouchBlock,
                     MainSliderBlock,
                     PortfolioBlock, PortfolioRecord, PortfolioType,
                     ProcessBlock, ProcessRecord,
                     ServiceBlock, ServiceRecord, Settings, SkillBlock,
                     SkillRecord, SlideRecord,
                     SocialRecord, TestimonialRecord, TestimonialsBlock,
                     VideoBlock,
                     WorkExperienceBlock, WorkExperienceRecord, SEO)

admin.site.register(AboutMeBlock)
admin.site.register(AwardsBlock)
admin.site.register(AwardRecord)
admin.site.register(CVBlock)
admin.site.register(EducationBlock)
admin.site.register(EducationRecord)
admin.site.register(GetInTouchBlock)
admin.site.register(MainSliderBlock)
admin.site.register(PortfolioBlock)
admin.site.register(PortfolioRecord)
admin.site.register(PortfolioType)
admin.site.register(ProcessBlock)
admin.site.register(ProcessRecord)
admin.site.register(ServiceBlock)
admin.site.register(ServiceRecord)
admin.site.register(Settings)
admin.site.register(SkillBlock)
admin.site.register(SkillRecord)
admin.site.register(SlideRecord)
admin.site.register(SocialRecord)
admin.site.register(TestimonialRecord)
admin.site.register(TestimonialsBlock)
admin.site.register(VideoBlock)
admin.site.register(WorkExperienceBlock)
admin.site.register(WorkExperienceRecord)
admin.site.register(SEO)
