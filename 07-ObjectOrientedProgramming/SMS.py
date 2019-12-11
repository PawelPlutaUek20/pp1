from message import Message
class SMS():
    def __init__(self,senders_phone_nr,receivers_phone_nr):
        self.senders_phone_nr = senders_phone_nr
        self.receivers_phone_nr = receivers_phone_nr
    def send(self, message):
        Message.set_message(self,message)
        print(f'''Wysyłanie SMSa...
Od: {self.senders_phone_nr}
Do: {self.receivers_phone_nr}
Treść: {self.message}''')