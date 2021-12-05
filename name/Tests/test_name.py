from flask import url_for
from unittest.mock import patch
from flask_testing import TestCase
from name import app
import requests


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_name(self):
        #response = self.client.get(url_for('name'), json={'random_name':'Ben'})
        #self.assertIn(b"Ben", response.data)

        with patch('random.randint') as g:
            g.return_value = 17
            response = self.client.get(url_for('name'))
            self.assertIn(b'Ry', response.data)


