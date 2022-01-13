from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def ping_pong():

    return render_template('index.html')


if __name__ == '__main__':

    app.run(host = '0.0.0.0', port = 8000, debug = True)
