from flask import Flask

app = Flask(__name__)

# localhost:8080/
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/name")
def name():
    return "<h1>Hi, I am Chol Mach from Enterprise Web Dev!</h1>"
