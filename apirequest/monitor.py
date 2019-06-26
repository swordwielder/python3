import smtplib
import requests

r = requests.get('http://chenpost.com/', timeout=5)
Email_address = os.environ.get('DB_USER')
Email_password = os.environ.get('DB_PASS')

# if r.status_code != 200:
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(Email_address, Email_password)

    subject = 'Check chenpost website'
    body = 'Restart the server and make sure it is back up'
    msg = (f"Subject: {subject}\n\n{body}")
    smtp.sendmail(Email_address, 'qchen125@gmail.com', msg)
