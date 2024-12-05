from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"
@app.route("anders")
def anders():
    return "<p>Een hele andere wereld</p>"