from flask import Flask, Response, request
from random import randint

app = Flask(__name__)

# generates name
@app.route('/fortune_finder/name', methods=['GET'])
def name():
    name = ["Anya", "Ben", "Charlie", "Daniel", "Ellie", "Francis", "George", "Hannah", "Izzy", "Joe", "Katie", "Liam", "Matthew", "Nathan", "Oliver", "Peter", "Quinn", "Ry", "Sophie", "Thomas", "Ulysses", "Valentine", "Wendy", "Xanthe", "Yohan", "Zoe"]
    random_name = names[randint(0,25)]
    return Response(random-name, mimetype="text/plain")


# generates prize
@app.route('/fortune_finder/prize', methods=['GET'])
def prize():
    if random-name[0] == 'A':
        prize = '£{}.random.randint(1,10)'
    elif random-name[0] == 'B':
        prize = '£{}.random.randint(2,20)'
    elif random-name[0] == 'C':
        prize = '£{}.random.randint(3,30)'
    elif random-name[0] == 'D':
        prize = '£{}.random.randint(4,40)'
    elif random-name[0] == 'E':
        prize = '£{}.random.randint(5,50)'
    elif random-name[0] == 'F':
        prize = '£{}.random.randint(6,60)'
    elif random-name[0] == 'G':
        prize = '£{}.random.randint(7,70)'
    elif random-name[0] == 'H':
        prize = '£{}.random.randint(8,80)'
    elif random-name[0] == 'I':
        prize = '£{}.random.randint(9,90)'
    elif random-name[0] == 'J':
        prize = '£{}.random.randint(10,100)'
    elif random-name[0] == 'K':
        prize = '£{}.random.randint(11,110)'
    elif random-name[0] == 'L':
        prize = '£{}.random.randint(12,120)'
    elif random-name[0] == 'M':
        prize = '£{}.random.randint(13,130)'
    elif random-name[0] == 'N':
        prize = '£{}.random.randint(14,140)'
    elif random-name[0] == 'O':
        prize = '£{}.random.randint(15,150)'
    elif random-name[0] == 'P':
        prize = '£{}.random.randint(16,160)'
    elif random-name[0] == 'Q':
        prize = '£{}.random.randint(17,170)'
    elif random-name[0] == 'R':
        prize = '£{}.random.randint(18,180)'
    elif random-name[0] == 'S':
        prize = '£{}.random.randint(19,190)'
    elif random-name[0] == 'T':
        prize = '£{}.random.randint(20,200)'
    elif random-name[0] == 'U':
        prize = '£{}.random.randint(21,210)'
    elif random-name[0] == 'V':
        prize = '£{}.random.randint(22,220)'
    elif random-name[0] == 'W':
        prize = '£{}.random.randint(23,230)'
    elif random-name[0] == 'X':
        prize = '£{}.random.randint(24,240)'
    elif random-name[0] == 'Y':
        prize = '£{}.random.randint(25,250)'
    elif random-name[0] == 'Z':
        prize = '£{}.random.randint(26,260)'
    return Response(prize, mimetype="text/plain")

# generates fortune
@app.route('/fortune_finder/fortune', methods=['Post'])
def fortune():
    if prize < 50 and prize > 0:
        future = "Will lose it to an online scam"
    elif prize < 100 and prize > 50:
        future = "Will lose it investing on a 'Big Chungus' NFT"
    elif prize < 150 and prize > 100:
        future = "Will lose it behind the sofa"
    elif prize < 250 and prize > 200:
        future = "Will lose it gambling on a turtle race"
    elif prize > 250:
        future = "Will lose it by spending the money on a new laptop that breaks the next day (didn't pay for the warranty)" 
    return Response(fortune, mimetype="text/plain")

print(name, prize, fortune)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')