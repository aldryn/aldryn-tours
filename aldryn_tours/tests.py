# -*- coding: utf-8 -*-
from django.conf import settings
from django.test import TestCase

from cms import api
from cms.test_utils.testcases import BaseCMSTestCase
from cms.utils import get_cms_setting

from .models import get_template


class RenderSnakeTestCase(TestCase, BaseCMSTestCase):
    def setUp(self):
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.page = api.create_page(
            'page', self.template, self.language, published=True
        )

    def test_render(self):
        response = self.client.get('/', follow=True)
        self.assertContains(response, '<!-- Aldryn Tour Head -->')
        self.assertContains(response, '<!-- Aldryn Tour Tail -->')

    def test_invalid_template(self):
        from aldryn_snake.template_api import registry
        rendered = get_template('none', None)
        registry.add_to_head(rendered)
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)
