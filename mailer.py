
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:

    SERVER_SMTP: str = '127.0.0.1'

    def __init__(self, remitente: str = '', destinatario: str = '', asunto: str = '', body: str = ''):
        self.remitente: str = remitente
        self.destinatario: str = destinatario
        self.asunto: str = asunto
        self.body: str = body

    def envia_email_html(self):
        msg: MIMEMultipart = self._crea_mimemultipart()
        msg.attach(MIMEText(self.body, 'html'))
        self._envia_mimemultipart(msg)

    def envia_email_plain(self):
        msg: MIMEMultipart
        msg = self._crea_mimemultipart()
        msg.attach(MIMEText(self.body, 'plain'))
        self._envia_mimemultipart(msg)

    def _envia_mimemultipart(self, msg: MIMEMultipart) -> None:
        server = smtplib.SMTP(Mailer.SERVER_SMTP)
        server.sendmail(self.remitente, self.destinatario, msg.as_string())
        server.quit()

    def _crea_mimemultipart(self) -> MIMEMultipart:
        msg: MIMEMultipart = MIMEMultipart()
        msg['From'] = self.remitente
        msg['To'] = self.destinatario
        msg['Subject'] = self.asunto
        return msg


