from flask import Flask, request
from ie_utils import tokenize


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world! Hey"

@app.route("/tokenize")
def do_tokenize():
    print(request.args)
    sentence = request.args["sentence"]
    lower = request.args.get("lower", False)
    return str(tokenize(sentence, lower = lower))