import smtplib
import os
import requests

Email_address = os.environ.get('DB_USER')
Email_password = os.environ.get('DB_PASS')
Token = os.environ.get('TOKEN')

def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(Email_address, Email_password)
        subject = 'Check chenpost website'
        body = 'Restart the server and make sure it is back up'
        msg = (f"Subject: {subject}\n\n{body}")
        smtp.sendmail(Email_address, 'qchen125@gmail.com', msg)

def reboot_server():
    #look up aws route 53 api
    print("rootboot the aws server")

try:
    r = requests.get('http://chenpost.com/', timeout=5)
    if r.status_code != 200:
        notify_user()
        reboot_server()
except Exception as e:
    notify_user()
    reboot_server()
