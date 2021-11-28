from flask import Flask, Response, request
from random import randint

app = Flask(__name__)

# generates name
@app.route('/fortune_finder/prize', methods=['GET'])
def prize():
    prize = random.randint(1,10)
    return Response(price, mimetype="text/plain")

