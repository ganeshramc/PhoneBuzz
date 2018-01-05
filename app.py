from flask import Flask, request, render_template, redirect
from make_call import MakeCalls


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
    delaymin = int(request.form["delaymin"])
    delay = int(request.form["delay"]) + delaymin*60
    MakeCalls.call_create(phno, delay)
    return redirect('/')


@app.route('/call/', methods=['GET','POST'])
def make_calls():
    return str(MakeCalls.play_game())

@app.route('/handle_call/', methods=['GET', 'POST'])
def handle_calls():
    digit_pressed = request.values.get('Digits', None)

    return str(MakeCalls.fizz_buzz_value(digit_pressed))



if __name__ == "__main__":
    app.run()
