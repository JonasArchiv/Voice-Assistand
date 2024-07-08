import smtplib
from email.message import EmailMessage

GmailAdressesender = ""  # Enter your Gmail Address
GMAILKEY = ""  # Enter your Gmail Password


def send(receiver, massage):
    msg = EmailMessage()
    msg.set_content(massage)

    msg["Subject"] = "Automatic E-Mail"
    msg["From"] = GmailAdressesender
    msg["To"] = receiver

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(GmailAdressesender, GMAILKEY)
    server.send_message(msg)
    server.quit()


send("test@test.com", "Hello World")
