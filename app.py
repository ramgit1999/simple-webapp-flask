import os
from flask import Flask
app = Flask(__name__)

...
...

color = "red"

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?' color=color

@app.route('/hi')
def hello2():
    return 'you are in myway'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
