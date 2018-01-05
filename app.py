from flask import Flask, request, render_template, redirect, abort
from make_call import MakeCalls, auth_token
from functools import wraps
from twilio.request_validator import RequestValidator
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('database.db')
conn.execute('DROP TABLE IF EXISTS history')
conn.execute('CREATE TABLE history (id INTEGER PRIMARY KEY AUTOINCREMENT, phno TEXT, delay INTEGER DEFAULT 0, number INTEGER DEFAULT 0, callsid TEXT)')

def validate_twilio_request(f):
    """Validates that incoming requests genuinely originated from Twilio"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Create an instance of the RequestValidator class
        validator = RequestValidator(auth_token)


        # Validate the request using its URL, POST data,
        # and X-TWILIO-SIGNATURE header
        request_valid = validator.validate(
            request.url,
            request.form,
            request.headers.get('X-TWILIO-SIGNATURE', ''))

        # Continue processing the request if it's valid, return a 403 error if
        # it's not
        if request_valid:
            return f(*args, **kwargs)
        else:
            return abort(403)
    return decorated_function

def print_rows():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM history")
    rows = list(cur.fetchall())
    for i in rows:
        print(list(i))


def select_last_row(callsid):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM history WHERE callsid=?", (callsid,))
    rows = list(cur.fetchall())

    for i in range(len(rows)):
        rows[i] = list(rows[i])

    return rows[-1]


@app.route('/')
def hello_world():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from history")

    rows = cur.fetchall()
    return render_template('main_page.html', rows=rows)

@app.route('/hello/<username>')
def yolo(username):
    return 'hellooooo '+ username


@app.route('/html_call/', methods=['POST'])
def main_html_call():
    phno = request.form["phno"]
    delaymin = int(request.form["delaymin"])
    delay = int(request.form["delay"]) + delaymin*60
    call = MakeCalls.call_create(phno, delay)
    if not call:
        con = sqlite3.connect('database.db')
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * from history")

        rows = cur.fetchall()
        return render_template('main_page_reverify.html', rows=rows)
    return redirect('/')


@app.route('/call/', methods=['GET','POST'])
@validate_twilio_request
def make_calls():
    return str(MakeCalls.play_game())


@app.route('/handle_call/', methods=['GET', 'POST'])
def handle_calls():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    digit_pressed = request.values.get('Digits', None)
    print_rows()
    print(request.values.get('CallSid'))
    row = select_last_row(request.values.get('CallSid', None))
    cur.execute("UPDATE history SET number=? WHERE callsid=?", (digit_pressed, request.values.get('CallSid')))
    con.commit()
    con.close()

    return str(MakeCalls.fizz_buzz_value(digit_pressed))

@app.route('/handle_table/', methods=['POST'])
def handle_table_input():
    phno = request.form["phno"]
    delaymin = int(request.form["delaymin"])
    digitpressed = int(request.form["number"])





if __name__ == "__main__":
    app.run()
