from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import namedtuple
from typing import List, Tuple
from autoEmailer.types import EmailText

class Message:

    def __init__(self, sender:str, recipient:str, subject:str, contentList:List[EmailText]):
        """
        Args:
            sender: the email address of the person sending the email
            recipient:  the email address of the person receiving the email
            subject: the subject of the email
            contentList: a list of objects containing the text in the body of the email as well as the type of text. 
                These pieces of text will appear in the same order in the email as they are in the list

                Example:
                contentList = [EmailText(text='random text', type='plain'), EmailText('random text'), EmailText('<p>random html</p>', 'html')]

        """
        self._sender = sender
        self._recipient = recipient
        self._subject = subject
        self._contentList = contentList

    @staticmethod
    def create(sender:str, recipient:str, subject:str, contentList:List[EmailText]):
        """
        Creates an email-ready message from the necessary components
        Args:
            sender: the email address of the person sending the email
            recipient:  the email address of the person receiving the email
            subject: the subject of the email
            contentList: a list of objects containing the text in the body of the email as well as the type of text. 
                These pieces of text will appear in the same order in the email as they are in the list

                Example:
                contentList = [EmailText(text='random text', type='plain'), EmailText('random text'), EmailText('<p>random html</p>', 'html')]

        """
        messageCreator = Message(sender, recipient, subject, contentList)
        messageCreator._createMIMEMessage()
        messageCreator._addContentToMessage()
        return messageCreator._message

    def _createMIMEMessage(self):
        self._message = MIMEMultipart()
        self._message['Subject'] = self._subject
        self._message['From'] = self._sender
        self._message['To'] = self._recipient

    def _addContentToMessage(self):
        for part in self._contentList:
            self._message.attach(MIMEText(part.text, part.type))



