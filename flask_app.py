from flask import Flask, request
import requests

app = Flask(__name__)

BOT_ID = 'd88d35ea841645b51035c369d1'  # Replace with your actual GroupMe bot ID
GROUPME_POST_URL = 'https://api.groupme.com/v3/bots/post'

BANNED_WORDS = [
    'clanker', 'clankers', 'clankin', 'clankin\'', 'clankinbot', 'clankoid', 'clank-mech', 'clanktrash',
    'damn', 'dam', 'd@mn',
    'hell', 'h3ll',
    'shit', 'sh*t', 'sh1t', 'sht', 's#!t',
    'fuck', 'f*ck', 'fuk', 'f***', 'f@ck', 'f#ck', 'fux', 'fck',
    'bitch', 'b!tch', 'biatch', 'b1tch', 'b*tch',
    'asshole', 'a**hole', 'ahole', 'ashole', 'azzhole',
    'dumbass', 'dumba**', 'dumb@ss', 'dumass',
    'bastard', 'b@stard', 'b*stard',
    'crap', 'cr@p',
    'douche', 'douchebag', 'doucheb@g', 'd0uche',
    'motherfucker', 'motherf***er', 'm*therf*cker', 'muthafucka', 'mofo'
]

def send_message(text):
    data = {
        "bot_id": BOT_ID,
        "text": text
    }
    requests.post(GROUPME_POST_URL, json=data)

@app.route('/', methods=['POST'])
def receive_message():
    msg = request.json
    text = msg.get('text', '').lower()
    sender = msg.get('name', 'Someone')

    for word in BANNED_WORDS:
        if word in text:
            send_message(f"⚠️ Hey {sender}, that word isn’t allowed in this group. Keep it clean or you will be removed .")
            break

    return "OK", 200

if __name__ == '__main__':
    app.run()
