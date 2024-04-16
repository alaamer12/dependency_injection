class SMSService:
    def __init__(self, sms_provider='Twilio'):
        self.sms_provider = sms_provider

    def send_sms(self, to_number, message):
        print(f"Sending SMS to {to_number} using {self.sms_provider}: {message}")
