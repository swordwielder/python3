import smtplib
import requests

r = requests.get('http://chenpost.com/', timeout=5)
Email_address = 'qifenchen@gmail.com'
Email_password = 'Well1170*'

if r.status_code != 200:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(Email_address, Email_password)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Restart the server and make sure it is back up'
        msg = (f"Subject: {subject}\n\n{body}")
    smtp.sendmail(Email_address, 'qchen125@gmail.com', msg)
