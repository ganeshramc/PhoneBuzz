from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say, Dial, Number
from twilio.base.exceptions import TwilioRestException
from threading import Timer
from credentials import *
import sqlite3





# put your own credentials here
# account_sid = "AC0dbebc41c0d4125a118b5f5958fc3c81"
# auth_token  = "290df12e2450cc200d9b1df988731e37"

client = Client(account_sid, auth_token)

class MakeCalls:

    @staticmethod
    def verify_phone_number(phone_number):
        """
        Verifying if a given phone number is valid or not
        :param phone_number: Phone number entered for player
        :return: If the phone number is valid
        """
        try:
            response = client.lookups.phone_numbers(phone_number).fetch(type="carrier")
            return True
        except TwilioRestException as e:
            if e.code == 20404:
                return False
            else:
                raise e

    @staticmethod
    def call_phone(phone_number, rowid):
        """
        Method to call the given phone number
        :param phone_number: Phone number of player
        :param rowid: row of the data
        :return: None
        """
        call = client.calls.create(to=phone_number,  # to your cell phone
                                   from_="+14086693946",  # from your Twilio phone number
                                   url="https://phone-fizz-buzz.herokuapp.com/call/")
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("UPDATE History SET callsid=? WHERE id=?", (str(call.sid), rowid))
        conn.commit()
        conn.close()



    @staticmethod
    def call_create(phone, delay):
        """
        Create a call on the database and set a timer for the call
        :param phone: phone number
        :param delay: delay (number of seconds)
        :return: If call went through
        """
        if not MakeCalls.verify_phone_number(phone):
            return False
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO History (phno, delay) VALUES (?,?)", (phone, delay))
        rowid = cur.lastrowid
        print(rowid)
        conn.commit()
        conn.close()
        t = Timer(delay, MakeCalls.call_phone, (phone,rowid))
        t.start()
        return True



    @staticmethod
    def play_game():
        """
        Playing the actual game by getting response from user
        :return: Digits received
        """
        response = VoiceResponse()
        with response.gather(action='/handle_call/', method='POST') as g:
            g.say("Please enter number followed by pound")

        return response

    @staticmethod
    def fizz_or_buzz(data):
        """
        If data is fizz or buzz or both or none
        :param data: number to check
        :return: string
        """
        if data % 5 == 0 and data % 3 == 0:
            return "Fizz, Buzz,"
        elif data % 3 == 0:
            return "Fizz,"
        elif data % 5 == 0:
            return "Buzz,"
        else:
            return str(data)+","


    @staticmethod
    def fizz_buzz_value(data):
        """
        Adding all the fizz buzz values for number 1 to given number
        :param data: given number
        :return: string of all data
        """
        message = ""
        data = int(data)
        response = VoiceResponse()

        for i in range(1, data+1):
            message += MakeCalls.fizz_or_buzz(i)

        response.say(message)

        return response



