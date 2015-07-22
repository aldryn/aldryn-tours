#!/usr/bin/env python
# -*- coding: utf-8 -*-

HELPER_SETTINGS = {
    'TIME_ZONE': 'Europe/Zurich',
    'INSTALLED_APPS': (
        'aldryn_tours',
        'aldryn_snake',
    ),
    'TEMPLATE_CONTEXT_PROCESSORS': (
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.i18n',
        'django.core.context_processors.debug',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.csrf',
        'django.core.context_processors.tz',
        'django.core.context_processors.static',
        'cms.context_processors.cms_settings',
        'aldryn_snake.template_api.template_processor'
    ),
    'TEMPLATE_DIRS': (
        'test_templates',
    ),
    'CMS_TEMPLATES': (
        ('base.html', 'Base'),
    ),
}


def run():
    from djangocms_helper import runner
    runner.cms('aldryn_tours')

if __name__ == "__main__":
    run()
