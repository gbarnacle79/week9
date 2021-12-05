from flask import Flask, request, Response, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql
#from server.models import Future



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fortune_finder.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)


class Future(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	prize = db.Column(db.String(30), nullable=False)
	fortune = db.Column(db.String(150), nullable=False)


db.drop_all()
db.create_all()



@app.route('/', methods=['GET'])
def fortune_finder():
    name = requests.get('http://name:5001/fortune_finder/name')
    prize = requests.get('http://prize:5002/fortune_finder/prize')
    fortune = requests.post('http://fortune:5003/fortune_finder/fortune', json = {"prize":prize.text, "name":name.text})
    db.session.add(Future(name = name.text, prize = prize.text, fortune = fortune.text))
    db.session.commit()
    a = db.session.query(Future).order_by(Future.id.desc()).limit(1).all()
    return render_template('index.html', name = name.text, prize = prize.text, fortune=fortune.text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)