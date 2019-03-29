import os
import requests
import random

import csv
DATA = []
with open('moods.csv') as file:
    cr = csv.DictReader(file)
    for line in cr:
        DATA.append(line)

API_TOKEN = os.environ['TG_API_TOKEN']
MOODS = [
    'tired', 'party', 'exploring', 'holy'
]
TABLE = pd.read_csv('./moods.csv')
LIMIT = 3

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

    def send_location(self, lat, lng):
        req = requests.post(
            'https://api.telegram.org/bot{token}/sendMessage'.format(token = API_TOKEN), 
            json={"chat_id": self.chat_id, "latitude": lat, "longitude": lng}
        )
        return req.text

    def start(self):
        self.send_message("Trabot is simple bot for users to get travel choices based on whatever is on his/her mind or mood. You can choose between the moods " + str(MOODS) + ".")
        self.send_message("You can choose between the following commands for now: ['/recommend', '/city', '/start']")

    def recommend(self, mood):
        self.send_message('We will help you get started with your upcoming trip!')
        r_index = int(random.random() * LIMIT)
        if mood == 'Exploring':
            r_index = 0 + r_index
        elif mood == 'Party':
            r_index = 3 + r_index
        elif mood == 'Tired':
            r_index = 6 + r_index
        elif mood == 'Holy':
            r_index = 9 + r_index
        name = DATA[r_index]['Name']
        latitude = DATA[r_index]['Latitude']
        longitude = DATA[r_index]['Latitude']
        self.send_message(name)
        self.send_location(latitude, longitude)

    def city(self):
        self.send_message("Once you plan your next city to travel, we'll assist you what will attract you there. :) ")
        self.send_message("This feature is in beta stage and will be available soon.")

    def do(self):
        if self.text.startswith('/start'):
            self.start()
        elif self.text.startswith('/recommend_tired'):
            self.recommend("Tired")
        elif self.text.startswith('/recommend_party'):
            self.recommend("Party")
        elif self.text.startswith('/recommend_exploring'):
            self.recommend("Exploring")
        elif self.text.startswith('/recommend_holy'):
            self.recommend("Holy")
        elif self.text.startswith('/city'):
            self.city()
