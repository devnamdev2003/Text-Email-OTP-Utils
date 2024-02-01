import vonage
import os
key = os.getenv('vonage_key')
secret = os.getenv('vonage_secret')
client = vonage.Client(key=key, secret=secret)
sms = vonage.Sms(client)
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "919926040407",
        "text": "hello pagal",
    }
)
if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")