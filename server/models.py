from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from server import db

class Future(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	prize = db.Column(db.String(30), nullable=False)
	fortune = db.Column(db.String(150), nullable=False, unique=True)
