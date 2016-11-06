# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161101_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='showSectionButtons',
        ),
        migrations.AddField(
            model_name='settings',
            name='show_animation',
            field=models.BooleanField(default=True, verbose_name='Использовать анимацию'),
        ),
        migrations.AddField(
            model_name='settings',
            name='show_section_buttons',
            field=models.BooleanField(default=True, verbose_name='Показывать кнопки секций'),
        ),
        migrations.AlterField(
            model_name='awardrecord',
            name='award_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.AwardsBlock', verbose_name='Блок наград'),
        ),
        migrations.AlterField(
            model_name='educationrecord',
            name='education_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.EducationBlock', verbose_name='Блок образования'),
        ),
        migrations.AlterField(
            model_name='portfoliorecord',
            name='portfolio_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.PortfolioBlock', verbose_name='Блок портфолио'),
        ),
        migrations.AlterField(
            model_name='processrecord',
            name='process_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.ProcessBlock', verbose_name='Блок процессов'),
        ),
        migrations.AlterField(
            model_name='servicerecord',
            name='service_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.ServiceBlock', verbose_name='Блок услуг'),
        ),
        migrations.AlterField(
            model_name='skillrecord',
            name='skill_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.SkillBlock', verbose_name='Блок навыков'),
        ),
        migrations.AlterField(
            model_name='sliderecord',
            name='main_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.MainSliderBlock', verbose_name='Блок слайдера'),
        ),
        migrations.AlterField(
            model_name='socialrecord',
            name='getintouch_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.GetInTouchBlock', verbose_name='Блок обратной связи'),
        ),
        migrations.AlterField(
            model_name='testimonialrecord',
            name='testimonial_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.TestimonialsBlock', verbose_name='Блок рекомендаций'),
        ),
        migrations.AlterField(
            model_name='workexperiencerecord',
            name='work_experience_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.WorkExperienceBlock', verbose_name='Блок опыта работы'),
        ),
    ]