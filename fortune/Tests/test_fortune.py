from flask import url_for
from unittest.mock import patch
from flask_testing import TestCase
from fortune import app
import requests

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_scam(self):
        response = self.client.post(url_for('fortune'), json={'name':'Anya', 'prize':'1'})
        self.assertIn(b'will lose it to an online scam', response.data)

    def test_invest(self):
        response = self.client.post(url_for('fortune'), json={'name':'Charlie', 'prize':'1'})
        self.assertIn(b"will lose it investing on a 'Big Chungus' NFT", response.data)

    def test_sofa(self):
        response = self.client.post(url_for('fortune'), json={'name':'Ben', 'prize':'7'})
        self.assertIn(b"will lose it behind the sofa", response.data)
            
    def test_turtle(self):
        response = self.client.post(url_for('fortune'), json={'name':'Daniel', 'prize':'7'})
        self.assertIn(b"will lose it gambling on a turtle race", response.data)
    

