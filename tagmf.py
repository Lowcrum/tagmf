import json
from flask import Flask
import flask
app = Flask(__name__)

def get_json_data(file_name):
    with open(file_name) as json_data:
        return json_data
        # d = json.load(json_data)
        # return d

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/list')
def list():
    data = get_json_data('aws_info.json')
    return data
