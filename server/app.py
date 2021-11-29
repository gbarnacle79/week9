from flask import Flask, request, Response, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('db_uri')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['SECRET_KEY'] = getenv('secretkey')

db = SQLAlchemy(app)



@app.route('/', methods=['GET'])
def fortune_finder():
    name = requests.get('http://name:5001/fortune_finder/name')
    prize = requests.get('http://prize:5002/fortune_finder/prize')
    fortune = requests.post('http://fortune:5003/fortune_finder/fortune', json = {"prize":prize.text, "name":name.text})
    return render_template('index.html', name=name.text, prize=prize.text, fortune=fortune.text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)