import os
import requests

class NotificationService:
    BASE_URL = os.getenv('BASE_URL')
    BOT_USER_ID = os.getenv('BOT_USER_ID')
    BOT_TOKEN = os.getenv('BOT_TOKEN')

    @staticmethod
    def send(roomId, message):
        if not NotificationService.BASE_URL or not NotificationService.BOT_USER_ID or not NotificationService.BOT_TOKEN:
            raise ValueError("BASE_URL, BOT_USER_ID, and BOT_TOKEN must be set")
        
        url = f"{NotificationService.BASE_URL}/api/v1/chat.postMessage"
        headers = {
            'X-User-Id': NotificationService.BOT_USER_ID,
            'X-Auth-Token': NotificationService.BOT_TOKEN,
            'Content-Type': 'application/json',
        }
        payload = {
            'roomId': roomId,
            'text': message
        }
        
        response = requests.post(url, json=payload, headers=headers)
        if not response.ok:
            raise Exception(f"Failed to send message: {response.text}")

# Example usage
# NotificationService.send(roomId="notifications", message="Hello world")
