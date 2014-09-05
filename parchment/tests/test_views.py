from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.utils import override_settings

from parchment.views import ParchmentView


class ParchmentViewTests(TestCase):
    valid_login = reverse('parchment_login') + '?student_id=12345678987654321&customers_dob=01/12/1980&customers_firstname=Joe&customers_lastname=Alumni&customers_email_address=joealumni@school.edu'
    invalid_login = reverse('parchment_login')

    def setUp(self):
        self.rf = RequestFactory()

    def test_view_template(self):
        """
        When a request is made to the login view, the correct template
        should be utilized.
        """
        request = self.rf.get(self.valid_login)
        response = ParchmentView.as_view()(request)
        self.assertTemplateUsed(response, 'parchment/login.html')

    def test_bad_response(self):
        """
        When an invalid request is made to the login view, it should return
        a 400 Bad Response.
        """
        request = self.rf.get(self.invalid_login)
        response = ParchmentView.as_view()(request)
        self.assertEquals(response.status_code, 400)

    def test_parch5_field(self):
        """
        When a valid request is made to the login view, it should contain
        a hidden ``parch5`` field.
        """
        request = self.rf.get(self.valid_login)
        response = ParchmentView.as_view()(request)
        self.assertContains(response, '<input id="id_parch5" name="parch5" type="hidden" value="')

    def test_parchiv_field(self):
        request = self.rf.get(self.valid_login)
        response = ParchmentView.as_view()(request)
        self.assertContains(response, '<input id="id_parchiv" name="parchiv" type="hidden" value="')

    @override_settings(PARCHMENT_DEBUG_MODE=True)
    def test_debug_field(self):
        request = self.rf.get(self.valid_login)
        response = ParchmentView.as_view()(request)
        self.assertContains(response, '<input id="id_debug" name="debug" type="hidden" value="')

    def test_action_url_s_id(self):
        request = self.rf.get(self.valid_login)
        response = ParchmentView.as_view()(request)
        self.assertContains(response, 's_id=1234567890abcdef')
