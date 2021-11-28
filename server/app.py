from flask import Flask, request, Response, render_template
import requests

app = Flask(__name__)



@app.route('/', methods=['GET'])
def fortune_finder():
    name = requests.get('http://fortune_finder:5000/fortune_finder/name')
    prize = requests.post('http://fortune_finder:5000/fortune_finder/prize', data=name.text)
    fortune = requests.get('http://fortune_finder:5000/fortune_finder/fortune', data = prize.txt)
    return render_template('index.html', name=name,text,prize=prize,text, fortune=fortune, text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)