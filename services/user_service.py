from .email_service import EmailService

class UserService:
    def __init__(self, email_service: EmailService = None):
        self.email_service = email_service

    def register_user(self, name: str, email: str):
        self.email_service.send_email(email, "Welcome to the platform!", f"Hi {name}, welcome aboard!")
