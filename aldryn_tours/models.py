# -*- coding: utf-8 -*-
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string

from aldryn_snake.template_api import registry


def get_template(name, request=None):
    try:
        return render_to_string('aldryn_tours/{}.html'.format(name))
    except TemplateDoesNotExist:
        return ''


def get_head(request=None):
    return get_template('head', request)


def get_tail(request=None):
    return get_template('tail', request)


registry.add_to_head(get_head)
registry.add_to_tail(get_tail)
