import os
import requests

class Sender:
    ROCKETCHAT_SERVER_URL = os.getenv('ROCKETCHAT_SERVER_URL')
    USER_ID = os.getenv('USER_ID')
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')

    @staticmethod
    def send(room_id, message):
        if not Sender.ROCKETCHAT_SERVER_URL or not Sender.USER_ID or not Sender.AUTH_TOKEN:
            raise ValueError("ROCKETCHAT_SERVER_URL, USER_ID, and AUTH_TOKEN must be set")
        
        url = f"{Sender.ROCKETCHAT_SERVER_URL}/api/v1/chat.postMessage"
        headers = {
            'X-User-Id': Sender.USER_ID,
            'X-Auth-Token': Sender.AUTH_TOKEN,
            'Content-Type': 'application/json',
        }
        payload = {
            'roomId': room_id,
            'text': message
        }
        
        response = requests.post(url, json=payload, headers=headers)
        if not response.ok:
            raise Exception(f"Failed to send message: {response.text}")
