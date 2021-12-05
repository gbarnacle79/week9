from flask import Flask, Response, request
import random

app = Flask(__name__)

# generates name
@app.route('/fortune_finder/prize', methods=['GET'])
def prize():
    prize = str(random.randint(1,10))
    return Response(prize, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)