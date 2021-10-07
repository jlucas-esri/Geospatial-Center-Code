import logging
import smtplib
from autoEmailer.message import Message
from autoEmailer.types import EmailText
from autoEmailer.secrets import PASSWORD
from email.mime.multipart import MIMEMultipart


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', "%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def setupServer(sender):
    server = smtplib.SMTP('smtp.example.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, PASSWORD)
    return server

def sendEmail(server:smtplib.SMTP, message:MIMEMultipart):
    logger.info('Sending email...')
    server.sendmail(message['From'], message['To'], message.as_string())
    logger.info('Email sent')

def main():
    sender = 'sender@example.com'
    recipient = 'receiver@example.com'
    subject = 'Text Email'

    plainText = 'This is some random plain text'

    htmlText = """\
    <html>
        <head></head>
        <body>
            <p>This is some random <strong>html</strong><p>
        </body>
    </html>
    """

    plainTextObject = EmailText(plainText, 'plain')
    htmlTextObject = EmailText(htmlText, 'html')
    
    logger.info('Creating message...')
    message = Message.create(sender, recipient, subject, [plainTextObject, htmlTextObject])
    logger.info('Message created')

    server = setupServer(sender)
    sendEmail(server, message)
    server.quit()
    

if __name__ == "__main__":
    main()
