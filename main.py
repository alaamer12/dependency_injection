from di_container import DIContainer
from app import App

# Create DI Container
container = DIContainer()

# Register Services
container.register_service('email_provider', 'Outlook')
container.register_service('sms_provider', 'Velo')

# Create App Instance
app_instance = container.create_instance(App)

# Use App
app_instance.notify_user("example@example.com", "+123456789", "Hello, world!")
