from flask import Flask, request, render_template, redirect, abort
from make_call import MakeCalls, auth_token
from functools import wraps
from twilio.request_validator import RequestValidator
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('database.db')
conn.execute('DROP TABLE IF EXISTS history')
conn.execute('CREATE TABLE history (id INTEGER PRIMARY KEY AUTOINCREMENT, phno TEXT, delay INT DEFAULT 0, number INT)')

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

def select_last_row(phone_number):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM history WHERE phone_number=?", (phone_number,))
    rows = cur.fetchall()
    if rows is None:
        return rows
    row = rows[-1]
    return row


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
    digit_pressed = request.values.get('Digits', None)
    row = select_last_row(request.values.get('From', None))
    conn.cursor().execute("INSERT INTO History (ID, number) VALUES (?,?)", (int(row["id"]), digit_pressed))
    return str(MakeCalls.fizz_buzz_value(digit_pressed))





if __name__ == "__main__":
    app.run()
