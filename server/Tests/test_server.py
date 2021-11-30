from flask import Flask, request, Response, render_template
import requests
import requests_mock
from flask import url_for
from unittest.mock import patch
from flask_testing import TestCase
from server.app import app, db, Future, fortune_finder
import requests

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",        
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Future(id=1,name = 'Ry', prize = '3', fortune = "will lose it to an online scam"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_fortune_finder(self):
        with requests_mock.Mocker() as m:
            m.get('http://name:5001/fortune_finder/name', text='Ry')
            m.get('http://prize:5002/fortune_finder/prize', text='3')
            m.post('http://fortune:5003/fortune_finder/fortune', text="will lose it to an online scam")
            response = self.client.get(url_for('fortune_finder'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Ry', response.data)
            self.assertIn(b'3', response.data)
            self.assertIn(b"will lose it to an online scam", response.data)