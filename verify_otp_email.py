import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


def genrate_otp(mail):
    otp = random.randint(100000, 999999)
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = mail
    msg['Subject'] = f"OTP velidation"
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>mail</title>
    </head>
    <body>
        <h1>Your OTP: <span>{otp}</span></h1>
    </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_USER, mail, msg.as_string())
    server.quit()
    return otp


mail = input('Enter your email address: ')
input('Press Enter to generate OTP ')
OTP = genrate_otp(mail)
print("Mail sent successfully Check your inbox...")
while (True):
    user_enterd_otp = int(input('Enter OTP: '))
    if user_enterd_otp == OTP:
        print("Verified")
        break
    else:
        print("invalid OTP Enter Again")
