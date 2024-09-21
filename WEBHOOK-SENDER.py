import requests
WEBHOOK_URL = input("Webhook URL: ")
while True:
    MESSAGE = input("Message: ")
    payload = {'content': MESSAGE}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(WEBHOOK_URL, json=payload, headers=headers)