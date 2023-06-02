import pytest
from unittest.mock import patch, ANY
from mailer import Mailer  # Asume que Mailer está definida en my_module

@patch("smtplib.SMTP")
def test_envia_email_html(mock_smtp):
    remitente = 'test@example.com'
    destinatario = 'dest@example.com'
    asunto = 'Test Subject'
    body = '<h1>Test Body</h1>'

    mailer = Mailer(remitente, destinatario, asunto, body)
    mailer.envia_email_html()

    mock_smtp.assert_called_once_with(Mailer.SERVER_SMTP)
    instance = mock_smtp.return_value
    instance.sendmail.assert_called_once_with(remitente, destinatario, ANY)
    instance.quit.assert_called_once()

@patch("smtplib.SMTP")
def test_envia_email_plain(mock_smtp):
    remitente = 'test@example.com'
    destinatario = 'dest@example.com'
    asunto = 'Test Subject'
    body = 'Test Body'

    mailer = Mailer(remitente, destinatario, asunto, body)
    mailer.envia_email_plain()

    mock_smtp.assert_called_once_with(Mailer.SERVER_SMTP)
    instance = mock_smtp.return_value
    instance.sendmail.assert_called_once_with(remitente, destinatario, ANY)
    instance.quit.assert_called_once()
