from services.email_service import EmailService
from services.sms_service import SMSService

class App:
    def __init__(self, email_service: EmailService, sms_service: SMSService):
        self.email_service = email_service
        self.sms_service = sms_service

    def notify_user(self, to_email, to_number, message):
        self.email_service.send_email(to_email, message)
        self.sms_service.send_sms(to_number, message)
