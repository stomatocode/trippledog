from flask import Flask
app = Flask(__name__)


@app.route('/')

def greeting():
    return 'Hello World!'


@app.route('/home')

def hello_world():
    return 'Hello World!'





if __name__ == '__main__':
    app.run()


# inbound SMS
# /message resources
# twitter API (consumer key: G2lHCk80bZzuIL2pf6d9AUsli)
#
