from flask import Flask, request, render_template
from make_call import MakeCalls, account_sid, auth_token
# from make_call import VoiceResponse, Gather,
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse, Say


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main_page.html')

@app.route('/hello/<username>')
def yolo(username):
    return 'hellooooo '+ username


@app.route('/html_call/', methods=['POST'])
def main_html_call():
    phno = request.form["phno"]
    client = Client(account_sid, auth_token)
    call = client.calls.create(to=phno,  # to your cell phone
                               from_="+14086693946",  # from your Twilio phone number
                               url="https://05b39715.ngrok.io/call/")

@app.route('/call/', methods=['GET','POST'])
def make_calls():
    return str(MakeCalls.play_game())

@app.route('/handle_call/', methods=['GET', 'POST'])
def handle_calls():
    digit_pressed = request.values.get('Digits', None)

    return str(MakeCalls.fizz_buzz_value(digit_pressed))



if __name__ == "__main__":
    app.run()
