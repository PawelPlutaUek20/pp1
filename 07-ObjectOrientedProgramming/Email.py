class Email():
    def __init__(self,senders_address,receivers_adress,theme):
        self.senders_address = senders_address
        self.receivers_address = receivers_adress
        self.theme = theme
    def send(self):
        