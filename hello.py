from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello yet again from Dockerised Flask"

@app.route("/hello")
def hi():
    caller=request.args.get('caller')
    return "Hello from {}".format(caller)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
