from flask import Flask, request, jsonify, redirect
import requests

import tg

BOT_USERNAME = 'trabotbot'

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect('https://t.me/{username}'.format(username = BOT_USERNAME)) 

@app.route('/updates', methods = ['POST'])
def updates():
    incoming = request.json
    chat_id = incoming['message']['chat']['id']
    text = incoming['message']['text']
    task = tg.Task(chat_id, text)
    task.do()
    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(port=8080, debug=True)