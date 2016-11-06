"""
Django settings for cv project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4v25^y9db^8uxm5_v%4-0uswnowgu92!d#&8%u*(b%on6@nngf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'debug_toolbar',
    'main',
    'easy_thumbnails',
    'pipeline',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'cv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            #os.path.join(BASE_DIR, 'main/templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.static',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'admin_tools.template_loaders.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'cv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'files', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'files', 'static')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

#STATICFILES_DIRS = ( os.path.join('static'), )

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
]

PIPELINE = {
    'PIPELINE_ENABLED': not DEBUG,
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',
    'STYLESHEETS': {
        'styles': {
            'source_filenames': (
                'main/css/bootstrap/bootstrap.min.css',
                'main/css/animations/animate.min.css',
                #'fonts/font-awesome/css/font-awesome.css',
                'main/fonts/font-awesome/css/font-awesome.min.css',
                'main/rs-plugin/css/settings.css',
                'main/rs-plugin/css/KenBurns.css',
                'main/css/stylesheet.css',
                'main/css/hide-show.css',
                'main/owl-carousel/owl-carousel/owl.carousel.css',
                'main/owl-carousel/owl-carousel/owl.theme.css',
                'main/css/portfolio/isotope-style.css',
                'main/lightbox/ekko-lightbox.css',
                'main/css/colors/green.css',
            ),
            'output_filename': 'main/css/styles.css',
        },
    },
    'JAVASCRIPT': {
        'scripts': {
            'source_filenames': (
                'main/js/jquery-1.11.2.js',
                'main/js/bootstrap.min.js',
                'main/js/animation/jquery.appear.js',
                'main/js/contact/contact-form.js',
                'main/lightbox/ekko-lightbox.js',
                'main/js/isotope/jquery.isotope.min.js',
                'main/js/isotope/custom-isotope.js',
                'main/rs-plugin/js/jquery.themepunch.plugins.min.js',
                'main/rs-plugin/js/jquery.themepunch.revolution.js',
                'main/owl-carousel/owl-carousel/owl.carousel.js',
                'main/js/custom.js',
                'main/js/parallex/script.js',
                'main/js/nav/jquery.scrollTo.js',
                'main/js/nav/jquery.nav.js',
                'main/js/sticky/jquery.sticky.js',
                'main/js/progress-bars/jquery.donutchart.js',
                'main/js/retina/retina.js',
                'main/js/jquery.fitvids.js',
            ),
            'output_filename': 'main/js/scripts.js',
        }
    }
}

INTERNAL_IPS = ('127.0.0.1', )
