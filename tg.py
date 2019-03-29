import os
import requests

API_TOKEN = os.environ['TG_API_TOKEN']
MOODS = [
    'happy', 'sad', 'tired', 'fresh', 'exploring', 'romantic'
]

class Task:
    chat_id = None
    text = None

    def __init__(self, chat_id, text):
        self.chat_id = chat_id
        self.text = text

    def send_message(self, message):
        req = requests.post(
            'https://api.telegram.org/bot{token}/sendMessage'.format(token = API_TOKEN), 
            json={"chat_id": self.chat_id, "text": message}
        )
        return req.text

    def start(self):
        self.send_message("Trabot is simple bot for users to get travel choices based on whatever is on his/her mind or mood. You can choose between the moods " + str(MOODS) + ".")

    def recommend(self):
        req = requests.post(
            'https://api.telegram.org/bot{token}/sendMessage'.format(token = API_TOKEN), 
            json={"chat_id": self.chat_id, "text": "Thanks for sharing :~", "reply_markup": {"one_time_keyboard": true,
            "keyboard": [[mood] for mood in MOODS]}}
        )
        return req.text

    def city(self):
        self.send_message("Coming soon.")

    def do(self):
        if self.text.starswith('/start'):
            self.start()
        elif self.text.startswith('/recommend'):
            self.recommend()
        elif self.text.startswith('/city'):
            self.city()
