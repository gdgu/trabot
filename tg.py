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
        self.send_message("You can choose between the following commands for now: ['/recommend', '/city', '/start']")

    def recommend(self):
        self.send_message('We will help you get started with your upcoming trip!')
        req = requests.post(
            'https://api.telegram.org/bot{token}/sendMessage'.format(token = API_TOKEN), 
            json={"chat_id": self.chat_id, "text": "Thanks for sharing :~", "reply_markup": {
            "inline_keyboard": [{"text": mood} for mood in MOODS]}}
        )
        return req.text

    def city(self):
        self.send_message("Once you plan your next city to travel, we'll assist you what will attract you there. :) ")
        self.send_message("This feature is in beta stage and will be available soon.")

    def do(self):
        if self.text.startswith('/start'):
            self.start()
        elif self.text.startswith('/recommend'):
            self.recommend()
        elif self.text.startswith('/city'):
            self.city()
