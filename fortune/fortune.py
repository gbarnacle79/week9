from flask import Flask, Response, request
from random import randint


app = Flask(__name__)


# generates fortune
@app.route('/fortune_finder/fortune', methods=['Post'])
def fortune():
    if prize < 5 and len(name) < 5:
        future = "Will lose it to an online scam"
    elif prize < 5 and len(name) > 5:
        future = "Will lose it investing on a 'Big Chungus' NFT"
    elif prize > 5 and len(name) < 5:
        future = "Will lose it behind the sofa"
    elif prize > 5 and len(name) > 5:
        future = "Will lose it gambling on a turtle race"    
    return Response(fortune, mimetype="text/plain")
