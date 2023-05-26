import requests
import json

TOKEN = '5870357601:AAGySmIthzxWxlJ5qHj2TPp3Raun7n-wPRk'

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, json=data)
    return response.json()

def handle_command(message):
    chat_id = message['chat']['id']
    command = message['text'].lower()

    if command == '/start':
        send_message(chat_id, 'Hello! How can I assist you?')
    elif command == '/help':
        send_message(chat_id, 'I can help you with various commands.')
    elif command == '/about':
        send_message(chat_id, 'I am a Telegram bot designed to assist users.')
    else:
        send_message(chat_id, 'Sorry, I didn\'t understand that command.')

def get_updates(offset=None):
    url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
    params = {'offset': offset, 'timeout': 60}
    response = requests.get(url, params=params)
    return response.json()

def main():
    last_update_id = 0

    while True:
        updates = get_updates(offset=last_update_id)

        if 'result' in updates and updates['result']:
            for update in updates['result']:
                if 'message' in update:
                    handle_command(update['message'])
                    last_update_id = update['update_id'] + 1

if __name__ == '__main__':
    main()