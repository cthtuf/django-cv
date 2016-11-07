# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutmeblock',
            options={'verbose_name': 'Блок Обо мне', 'verbose_name_plural': 'Блок Обо мне'},
        ),
        migrations.AlterModelOptions(
            name='awardsblock',
            options={'verbose_name': 'Блок Награды', 'verbose_name_plural': 'Блок Награды'},
        ),
        migrations.AlterModelOptions(
            name='cvblock',
            options={'verbose_name': 'Блок Резюме', 'verbose_name_plural': 'Блок Резюме'},
        ),
        migrations.AlterModelOptions(
            name='educationblock',
            options={'verbose_name': 'Блок Образование', 'verbose_name_plural': 'Блок Образование'},
        ),
        migrations.AlterModelOptions(
            name='getintouchblock',
            options={'verbose_name': 'Блок Обратная связь', 'verbose_name_plural': 'Блок Обратная связь'},
        ),
        migrations.AlterModelOptions(
            name='mainsliderblock',
            options={'verbose_name': 'Блок Слайдер', 'verbose_name_plural': 'Блок Слайдер'},
        ),
        migrations.AlterModelOptions(
            name='portfolioblock',
            options={'verbose_name': 'Блок Портфолио', 'verbose_name_plural': 'Блок Портфолио'},
        ),
        migrations.AlterModelOptions(
            name='processblock',
            options={'verbose_name': 'Блок Процессы', 'verbose_name_plural': 'Блок Процессы'},
        ),
        migrations.AlterModelOptions(
            name='serviceblock',
            options={'verbose_name': 'Блок Услуги', 'verbose_name_plural': 'Блок Услуги'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Настройки сайта', 'verbose_name_plural': 'Настройки сайта'},
        ),
        migrations.AlterModelOptions(
            name='skillblock',
            options={'verbose_name': 'Блок Навыки', 'verbose_name_plural': 'Блок Навыки'},
        ),
        migrations.AlterModelOptions(
            name='testimonialrecord',
            options={'ordering': ('index',), 'verbose_name': 'Рекомендация', 'verbose_name_plural': 'Рекомендации'},
        ),
        migrations.AlterModelOptions(
            name='testimonialsblock',
            options={'verbose_name': 'Блок Рекомендации', 'verbose_name_plural': 'Блок Рекомендации'},
        ),
        migrations.AlterModelOptions(
            name='videoblock',
            options={'verbose_name': 'Блок Видео', 'verbose_name_plural': 'Блок Видео'},
        ),
        migrations.AlterModelOptions(
            name='workexperienceblock',
            options={'verbose_name': 'Блок Опыт работы', 'verbose_name_plural': 'Блок Опыт работы'},
        ),
    ]
