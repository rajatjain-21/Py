from flask import Flask     #Installing flask dependency
app = Flask(__name__)       #creating an instance of flask app. "__name__" evaluates to a string that names a Flask app

@app.route("/")             #setting up a route / on our App

def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)