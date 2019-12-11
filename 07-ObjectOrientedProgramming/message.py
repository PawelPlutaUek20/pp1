class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        self.message = message.capitalize()
        self.message = self.message + " BYE."