from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse, Say

# put your own credentials here
account_sid = "AC0dbebc41c0d4125a118b5f5958fc3c81"
auth_token  = "290df12e2450cc200d9b1df988731e37"

# # set up a client to talk to the Twilio REST API
# client = Client(account_sid, auth_token)
#
# call = client.calls.create(to="+19494197775",    # to your cell phone
#                            from_="+14086693946", # from your Twilio phone number
#                            url="https://www.twilio.com/docs/twiml-snippet/quickstart")


class MakeCalls:

    @staticmethod
    def play_game():
        response = VoiceResponse()
        gather = Gather(action='/process_gather.php', method='GET')
        gather.say("Please enter number followed by pound")
        response.append(gather)
        response.say(response)
        return response

    @staticmethod
    def fizz_buzz_value(data):
        if data % 5 == 0 and data % 3 == 0:
            return "Fizz, Buzz"
        elif data % 3 == 0:
            return "Fizz"
        elif data % 5 == 0:
            return "Buzz"
        else:
            return str(data)

