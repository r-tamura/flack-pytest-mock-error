from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    json = request.get_json()
    print(json)
    return "<p>Hello, World!</p>"

