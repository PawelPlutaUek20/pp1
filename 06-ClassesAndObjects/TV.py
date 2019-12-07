class TV:
    def __init__(self):
        self.is_on = "wyłączony"
        self.channel_no = 1
        self.channels = []
        self.volume = 0
        
    def on(self):
        self.is_on = "załączony"
        
    def off(self):
        self.is_on = "wyłączony"
        
    def show_status(self):
        print("Odbiornik TV jest " + self.is_on, end='')
        if self.is_on == "załączony":
            print(", kanał " + str(self.channel_no), end= '')
            if self.channel_no in range(len(self.channels)):     
                print(" ("+self.channels[self.channel_no-1] + ")")
            else:
                print()
            print("poziom glosnosci:", self.volume)
        else:
            print()
            
    def set_channel(self,new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, channels_list):
        self.channels.append(channels_list)
        
    def show_channels(self):
        print("LISTA KANAŁÓW TV")
        for i in range(len(self.channels)):
            print(str(i+1), self.channels[i])
            
    def volume_up(self):
        if self.volume in range(10):
            self.volume += 1

    def volume_down(self):
        if self.volume in range(1,11):
            self.volume -= 1