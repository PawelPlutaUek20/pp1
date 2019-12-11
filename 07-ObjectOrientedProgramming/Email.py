from message import Message
class Email(Message):
    def __init__(self,senders_address,receivers_adress,theme):
        self.senders_address = senders_address
        self.receivers_address = receivers_adress
        self.theme = theme
    def send(self,message):
        Message.set_message(self,message)
        print(f'''Wysyłanie emaila...
Od: {self.senders_address}
Do: {self.receivers_address}
Temat: {self.theme}
Treść: {self.message}''')
        
x = Email("nowak@onet.pl", "kowalski@gmail.com", "Spotkanie w czwartek", )
x.send("informuję, że nasze czwartkowe spotkanie zostało odwołane.")
        