import requests

class WhatsappService:
    def __init__(self, token: str, phone_number_id: str):
        self.token = token
        self.phone_number_id = phone_number_id

    def send_message(self, to: str, message: str):
        url = f"https://graph.facebook.com/v18.0/{self.phone_number_id}/messages"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": message}
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
