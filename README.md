# PhoneBuzz
A phone implementation of Fizz Buzz

A general description of the game from Wikipedia: 
Players generally sit in a circle. The player designated to go first says the number "1", and each player counts one number in turn. However, any number divisible by three is replaced by the word fizz and any divisible by five by the word buzz. Numbers divisible by both become fizz buzz. A player who hesitates or makes a mistake is eliminated from the game.

For example, a typical round of fizz buzz would start as follows:

    1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...


## Play the game
Two ways to play the game:
1) To receive a call visit (https://phone-fizz-buzz.herokuapp.com/) 
2) Call +1 (408) 669-3946
 
## To set up game for yourself
1) Clone the repository
2) Activate virtualenv by going to the root folder of the game and typing the command source venv/bin/activate
3) Set up your own environment variables for twilio credentials. This is very important You would perform the following commands in the terminal:
..1) `export TWILIO_AUTH_TOKEN='YOUR TWILIO AUTHENTICATION TOKEN'`
..2) `export TWILIO_ACCOUNT_SID='YOUR TWILIO ACCOUNT SID'`
4) You can run it on localhost with the command `python app.py`
5) You might also want to host your app on a server using services like Heroku, AWS or ngrok...
6) Enjoy!
