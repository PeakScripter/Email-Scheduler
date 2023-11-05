import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    sender_email = 'youremail@gmail.com'
    sender_password = 'yourpassword'
    receiver_email = 'receiveremail@gmail.com'
    subject = input('Subject: ')
    file = open("conf", "r")
    message = file.read()
    file.close()

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

schedule.every().day.at("08:00").do(send_email)
while True:
    schedule.run_pending()
    time.sleep(1)
