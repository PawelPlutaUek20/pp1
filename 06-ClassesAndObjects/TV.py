class Telewizor():
    def __init__(self):
        self.name = "Telewizor"
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def show_status(self):
        print(self.name, "jest",end=' ')
        if self.is_on:
            print("załączony", end=',')
            print(" kanał", self.channel_no,end=' ')
            if self.channel_no in range(len(self.channels)+1):
                print("(" + self.channels[self.channel_no-1] + ')',end=', ')
            else:
                print(', ',end='')
            print("poziom głosności: " + str(self.volume))
        elif not self.is_on:
            print("wyłączony")
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self, channels_list):
        self.channels.append(channels_list)
    def show_channels(self):
        print("LISTA KANAŁÓW TV")
        for i in range(len(self.channels)):
            print(str(i+1) + ". " + self.channels[i])
    def volume_up(self):
        if self.volume in range(10):
            self.volume+=1
    def volume_down(self):
        if self.volume in range(1,11):
            self.volume-=1
tv = Telewizor()
tv.show_status()
tv.on()
tv.show_status()
tv.set_channel(5)
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_up()
tv.volume_down()
tv.show_status()
tv.show_channels()
tv.set_channels("TVP1")
tv.set_channels("TVP2")
tv.set_channels("Polsat")
tv.set_channels("TVN")
tv.set_channels("Filmbox")
tv.show_channels()
tv.show_status()
tv.off()
tv.show_status()