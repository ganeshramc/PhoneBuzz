from flask import Flask, request
from make_call import MakeCalls
# from make_call import VoiceResponse, Gather,
from twilio.twiml.voice_response import Play, VoiceResponse, Say


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Dummy!!!!!!!'

@app.route('/hello/<username>')
def yolo(username):
    return 'hellooooo '+ username


@app.route('/call/', methods=['GET','POST'])
def make_calls():
    return str(MakeCalls.play_game())

@app.route('/handle_call/', methods=['GET', 'POST'])
def handle_calls():
    digit_pressed = request.values.get('Digits', None)

    return str(MakeCalls.fizz_buzz_value(digit_pressed))



if __name__ == "__main__":
    app.run()
