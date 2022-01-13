from flask import Flask
import json


app = Flask(__name__)


@app.route('/')
def ping_pong():

    result = {
        "ping" : "pong"
    }

    return result


if __name__ == '__main__':

    app.run(host='0.0.0.0', port = 9000, debug = True)
