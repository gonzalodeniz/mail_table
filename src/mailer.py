import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, sender_email):
        self.sender_email = sender_email

    def send_email(self, recipient_email, subject, body, is_html=False):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        if is_html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('localhost')
        text = msg.as_string()
        server.sendmail(self.sender_email, recipient_email, text)
        server.quit()

def main():
    sender_email = "soygonzalodeniz@gmail.com"
    recipient_email = "liboc36285@rockdian.com"
    subject = "Hello"
    body = "<h1>This is a test email.</h1>"

    mailer = Mailer(sender_email)
    mailer.send_email(recipient_email, subject, body, is_html=True)

if __name__ == "__main__":
    main()