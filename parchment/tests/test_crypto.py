from __future__ import unicode_literals

import re

from django.test import TestCase

from parchment.crypto import Parchment


class ParchmentTests(TestCase):
    def setUp(self):
        self.key = 'dpYeodnsgmaOav5fsqN7bhZM8W8hoaBM'
        self.iv = '6162636465666768696a6b6c6d6e6f70'
        self.request = 'ts=2013-10-31T13:31:22+00:00&student_id=12345678987654321&customers_dob=01/12/1980&customers_firstname=Joe&customers_lastname=Alumni&customers_email_address=joealumni@school.edu&rand=YDXNHYYXB2OELFSQ'

    def test_encrypt(self):
        """
        When initialized with a known initialization vector, the given
        request string should encode to a known hex encoded encrypted
        value.
        """
        p = Parchment(self.key, iv=self.iv)
        self.assertEqual(p.encrypt(self.request), '0e818ec14c1e3390359c249e44fb052256daea18bc42d4d4a66d7af26f0957f65e333316c4e4b4063af7a7a15f891f627cb2bd883d8b069c9f3f1091b3b213ae8fcc103c11bd09414dd4795c871ad2974e154befe8bab6ad570556d592e6d8b6e4c0f8e23370d5e3950ccaba4c28fb198b04cde124c6f95647188faace8729ffb864223258368e8cb976033b95aab2cecfb9a353f09e41f051d85c48507c06a2d29f545b60dd0f86dcc94f34377a3e202271379769d58d88608bfe9e167aa0c6f6926dba749807cfaae1672b37003e8f')

    def test_iv(self):
        """
        An instance should contain a randomized hex encoded
        initialization vector.
        """
        p = Parchment(self.key)
        self.assertTrue(re.search('^[0-9a-f]{32}$', p.iv))
