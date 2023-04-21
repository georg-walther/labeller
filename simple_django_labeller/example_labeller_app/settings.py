"""
Django settings for example_labeller_app project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from image_labelling_tool import labelling_tool

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3+p2$qln6o1ws1c)6o!+o+p%ql1n!+tt@wp)g5!pfgliqld)yo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'image_labelling_tool.apps.ImageLabellingToolConfig',
    'example_labeller.apps.ExampleLabellerConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'example_labeller_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'example_labeller_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CSRF_COOKIE_SECURE = False

#
#
# Colour schemes and label classes are stored in the database
#
#


# Annotation controls
# Labels may also have optional meta-data associated with them
# You could use this for e.g. indicating if an object is fully visible, mostly visible or significantly obscured.
# You could also indicate quality (e.g. blurriness, etc)
# There are four types of annotation. They have some common properties:
#   - name: symbolic name (Python identifier)
#   - label_text: label text in UI
#   Check boxes, radio buttons and popup menus also have:
#     - visibility_label_text: [optional] if provided, label visibility can be filtered by this annotation value,
#       in which case a drop down will appear in the UI allowing the user to select a filter value
#       that will hide/show labels accordingly
# Control types:
# Check box (boolean value):
#   `labelling_tool.AnnoControlCheckbox`; only the 3 common parameters listed above
# Radio button (choice from a list):
#   `labelling_tool.AnnoControlRadioButtons`; the 3 common parameters listed above and:
#       choices: list of `labelling_tool.AnnoControlRadioButtons.choice` that provide:
#           value: symbolic value name for choice
#           tooltip: extra information for user
#       label_on_own_line [optional]: if True, place the label and the buttons on a separate line in the UI
# Popup menu (choice from a grouped list):
#   `labelling_tool.AnnoControlPopupMenu`; the 3 common parameters listed above and:
#       groups: list of groups `labelling_tool.AnnoControlPopupMenu.group`:
#           label_text: label text in UI
#           choices: list of `labelling_tool.AnnoControlPopupMenu.choice` that provide:
#               value: symbolic value name for choice
#               label_text: choice label text in UI
#               tooltip: extra information for user
# Text (free form plain text):
#   `labelling_tool.AnnoControlText`; only the 2 common parameters listed above and:
#       - multiline: boolean; if True a text area will be used, if False a single line text entry
ANNO_CONTROLS = [
    labelling_tool.AnnoControlCheckbox('good_quality', 'Good quality',
                                       visibility_label_text='Filter by good quality'),
    labelling_tool.AnnoControlRadioButtons('visibility', 'Visible', choices=[
        labelling_tool.AnnoControlRadioButtons.choice(value='full', label_text='Fully',
                                                      tooltip='Object is fully visible'),
        labelling_tool.AnnoControlRadioButtons.choice(value='mostly', label_text='Mostly',
                                                      tooltip='Object is mostly visible'),
        labelling_tool.AnnoControlRadioButtons.choice(value='obscured', label_text='Obscured',
                                                      tooltip='Object is significantly obscured'),
    ], label_on_own_line=False, visibility_label_text='Filter by visibility'),
    labelling_tool.AnnoControlPopupMenu('material', 'Material', groups=[
        labelling_tool.AnnoControlPopupMenu.group(label_text='Artificial', choices=[
            labelling_tool.AnnoControlPopupMenu.choice(value='coil', label_text='Coil',
                                                       tooltip='Coil'),
            labelling_tool.AnnoControlPopupMenu.choice(value='stent', label_text='Stent',
                                                       tooltip='Stent'),
            labelling_tool.AnnoControlPopupMenu.choice(value='clip', label_text='Clip',
                                                       tooltip='Clip'),
        ]),
        labelling_tool.AnnoControlPopupMenu.group(label_text='Natural', choices=[
            labelling_tool.AnnoControlPopupMenu.choice(value='aneurysm', label_text='Aneurysm',
                                                       tooltip='Aneurysm'),
            labelling_tool.AnnoControlPopupMenu.choice(value='harbouring-vessel',
                                                       label_text='Harbouring Vessel',
                                                       tooltip='Harbouring Vessel'),
            labelling_tool.AnnoControlPopupMenu.choice(value='thrombus', label_text='Thrombus',
                                                       tooltip='Thrombus'),
            labelling_tool.AnnoControlPopupMenu.choice(value='SAH', label_text='Subarachnoid Hemorrhage',
                                                       tooltip='Subarachnoid Hemorrhage'),
            labelling_tool.AnnoControlPopupMenu.choice(value='tumor', label_text='Tumor',
                                                       tooltip='Tumor'),
            labelling_tool.AnnoControlPopupMenu.choice(value='cerebral-anomaly', label_text='Cerebral Anomaly',
                                                       tooltip='Cerebral Anomaly')]),
    ], visibility_label_text='Filter by material'),
    # labelling_tool.AnnoControlText('comment', 'Comment', multiline=False),
]

# Configuration
LABELLING_TOOL_CONFIG = {
    'useClassSelectorPopup': True,
    'tools': {
        'imageSelector': True,
        'labelClassSelector': True,
        'brushSelect': True,
        'labelClassFilter': True,
        'drawPointLabel': False,
        'drawBoxLabel': True,
        'drawOrientedEllipseLabel': True,
        'drawPolyLabel': True,
        'deleteLabel': True,
        'deleteConfig': {
            'typePermissions': {
                'point': True,
                'box': True,
                'polygon': True,
                'composite': True,
                'group': True,
            }
        }
    },
    'settings': {
        'brushWheelRate': 0.01,  # Change rate for brush radius (mouse wheel)
        'brushKeyRate': 2.0,  # Change rate for brush radius (keyboard)
    }
}

LABELLING_TOOL_ENABLE_LOCKING = False
LABELLING_TOOL_DEXTR_AVAILABLE = False
LABELLING_TOOL_DEXTR_POLLING_INTERVAL = 1000
LABELLING_TOOL_DEXTR_WEIGHTS_PATH = None

LABELLING_TOOL_EXTERNAL_LABEL_API = False
LABELLING_TOOL_EXTERNAL_LABEL_API_URL = 'http://localhost:3000/get_labels'

CELERY_BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'rpc://'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
