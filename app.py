from flask import Flask
from flask import request
from make_call import MakeCalls
# from make_call import VoiceResponse, Gather
from twilio.twiml.voice_response import Play, VoiceResponse, Say


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Dummy!!!!!!!'


@app.route('/hello1')
def print_hello():
    return 'Helloooookadhfoiae'

@app.route('/hello1/<username>')
def print_hello1(username):
    return 'Helle' + username


@app.route('/hello/<username>')
def yolo(username):
    return 'hellooooo '+ username


@app.route('/make_direct_call/', methods=['GET','POST'])
def make_calls():
    print(MakeCalls.play_game())



if __name__ == "__main__":
    app.run()