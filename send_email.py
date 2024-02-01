import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

#  take input
email=input('Email address: ')
name=input('Name: ')
message=input('Message: ')

msg = MIMEMultipart()
msg['From'] = EMAIL_USER
msg['To'] = email
msg['Subject'] = f"Mail from {name}"

# set mail body 
body=f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>mail</title>
</head>
<body>
    <h1>Message: <span>{message}</span></h1>
</body>
</html>
"""

msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()
server.login(EMAIL_USER, EMAIL_PASSWORD)
server.sendmail(EMAIL_USER, email, msg.as_string())
server.quit()

print("Mail sent successfully")