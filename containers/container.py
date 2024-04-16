from injector import Module, singleton, Injector
from services.email_service import EmailService
from services.user_service import UserService

class MainModule(Module):
    def configure(self, binder):
        binder.bind(EmailService, to=EmailService, scope=singleton)
        binder.bind(UserService, to=UserService, scope=singleton)

def create_injector() -> Injector:
    return Injector([MainModule()])
