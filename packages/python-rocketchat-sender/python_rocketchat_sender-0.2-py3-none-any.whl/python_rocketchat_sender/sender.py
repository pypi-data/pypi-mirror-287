import os
import requests

class Sender:
    ROCKETCHAT_SERVER_URL = os.getenv('ROCKETCHAT_SERVER_URL')
    BOT_USER_ID = os.getenv('BOT_USER_ID')
    BOT_TOKEN = os.getenv('BOT_TOKEN')

    @staticmethod
    def send(room_id, message):
        if not Sender.ROCKETCHAT_SERVER_URL or not Sender.BOT_USER_ID or not Sender.BOT_TOKEN:
            raise ValueError("ROCKETCHAT_SERVER_URL, BOT_USER_ID, and BOT_TOKEN must be set")
        
        url = f"{Sender.ROCKETCHAT_SERVER_URL}/api/v1/chat.postMessage"
        headers = {
            'X-User-Id': Sender.BOT_USER_ID,
            'X-Auth-Token': Sender.BOT_TOKEN,
            'Content-Type': 'application/json',
        }
        payload = {
            'roomId': room_id,
            'text': message
        }
        
        response = requests.post(url, json=payload, headers=headers)
        if not response.ok:
            raise Exception(f"Failed to send message: {response.text}")
