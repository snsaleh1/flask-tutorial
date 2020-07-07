from flask import Flask


@app.route('/')
def hello():
    return 'Hello, World!'

app = Flask(__name__)