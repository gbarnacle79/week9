from flask import url_for
from unittest.mock import patch
from flask_testing import TestCase
from prize import app
import requests

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_prize(self):
        with patch('random.randint') as g:
            g.return_value = 7
            response = self.client.get(url_for('prize'))
            self.assertIn(b'7', response.data)


