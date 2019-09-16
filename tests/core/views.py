# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext as _
from django.views.generic import (
    TemplateView,
)
from cookie_consent.util import get_cookie_value_from_request , js_cookie_consent_receipts

COOKIE_RECEIPTS_USED = {
    'analytic': {
        'domain': '*.google.com',
        'title_law': _('Title Law'),
        'content_law': _('Content Law'),
        } ,
     'social': {
        'title_law': _('Title Law'),
        'content_law': _('Content Law'),
       },
     }

class TestPageView(TemplateView):
    template_name = "test_page.html"

    def get(self, request, *args, **kwargs):
        response = super(TestPageView, self).get(request, *args, **kwargs)
        if get_cookie_value_from_request(request, "optional") is True:
            val = "optional cookie set from django"
            response.set_cookie("optional_test_cookie", val)
        return response

class TestPageViewReceipts(TemplateView):
    template_name = "test_page_with_cookie_receipts.html"

    def get(self, request, *args, **kwargs):
        response = super(TestPageViewReceipts, self).get(request, *args, **kwargs)
        if get_cookie_value_from_request(request, "optional") is True:
            val = "optional cookie set from django"
            response.set_cookie("optional_test_cookie", val)
            js_cookie_consent_receipts( 'optional' , request)
        return response
