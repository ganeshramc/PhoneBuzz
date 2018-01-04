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


@app.route('/make_direct_call/')
def make_calls():
    response = VoiceResponse()
    response.say(message="Hello Ganesh")
    response.play('https://api.twilio.com/Cowbell.mp3')
    return response
    # return MakeCalls.play_game()
    # return 'Hello'



if __name__ == "__main__":
    app.run()
