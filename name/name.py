from flask import Flask, Response, request
from random import randint

app = Flask(__name__)

# generates name
@app.route('/fortune_finder/name', methods=['GET'])
def name():
    name = ["Anya", "Ben", "Charlie", "Daniel", "Ellie", "Francis", "George", "Hannah", "Izzy", "Joe", "Katie", "Liam", "Matthew", "Nathan", "Oliver", "Peter", "Quinn", "Ry", "Sophie", "Thomas", "Ulysses", "Valentine", "Wendy", "Xanthe", "Yohan", "Zoe"]
    random_name = names[randint(0,25)]
    return Response(random_name, mimetype="text/plain")

print(random_name)