# class EmailService:
#     def send_email(self, to_email: str, subject: str, body: str):
#         print(f"Sending email to {to_email} with subject '{subject}' and body '{body}'")

class EmailService:
    def __init__(self, email_provider='Gmail'):
        self.email_provider = email_provider

    def send_email(self, to_email, message):
        print(f"Sending email to {to_email} using {self.email_provider}: {message}")
