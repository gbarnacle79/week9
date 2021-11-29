from flask import Flask, Response, request
from random import randint


app = Flask(__name__)


# generates fortune
@app.route('/fortune_finder/fortune', methods=['Post'])
def fortune():
    prize=request.get_json()["prize"]
    name=request.get_json()["name"]
    if int(prize) < 5 and len(name) < 5:
        answer = "will lose it to an online scam"
    elif int(prize) < 5 and len(name) > 5:
        answer = "will lose it investing on a 'Big Chungus' NFT"
    elif int(prize) > 5 and len(name) < 5:
        answer = "will lose it behind the sofa"
    elif int(prize) > 5 and len(name) > 5:
        answer = "will lose it gambling on a turtle race"    
    return Response(answer, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)