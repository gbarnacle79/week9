from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:[PASSWORD]@mysql:3306/flask-db'

class Fortune(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	prize = db.Column(db.String(30), nullable=False)
	fortune = db.Column(db.String(150), nullable=False, unique=True)
	def __repr__(self):
		return ''.join(['ID : ', str(self.id), '\r\n', 'Name : ', self.name, ' Prize : ', self.prize, 'Fortune : ', self.fortune '\n'])

