import vlc
import threading
import serial
from pyModbus import pyModbus
import os
from time import sleep

class Player():
    """vlc_python library
    https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.MediaPlayer-class.html
    """
    def __init__(self):
        # Create a basic vlc instance
        self.instance = vlc.Instance('--input-repeat=-1')

        self.media = None

        # Create an empty vlc media player
        self.mediaplayer = self.instance.media_player_new()
        self.is_paused = False
        #Set full screen
        self.mediaplayer.set_fullscreen(True)

    def play_only(self):

        if self.is_paused is True:
            print("Play the video")
            self.mediaplayer.play()
            self.is_paused = False

    def pause_only(self):
        if self.mediaplayer.is_playing():
            print("Pause the video")
            self.mediaplayer.pause()
            self.is_paused = True

    def play_pause(self):
        """Toggle play/pause status
        """
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.is_paused = True
        else:
            # if self.mediaplayer.play() == -1:
            #     self.open_file()
            #     return
            self.mediaplayer.play()
            self.is_paused = False

    def stop(self):
        """Stop player
        """
        self.mediaplayer.stop()

    def open_file(self, path):
        """Open a media file in a MediaPlayer
        """
        # getOpenFileName returns a tuple, so use only the actual file name
        self.media = self.instance.media_new(path)
        # Put the media in the media player
        self.mediaplayer.set_media(self.media)
        #self.stop()
        self.play_pause()
        print("open video: " + path)

def main_vlc():
    """Entry point for our simple vlc player
    """
    filename = ["./videos/01.mp4", "./videos/02.mp4", "./videos/03.mp4"]

    player = Player()
    player.open_file(filename[0])

    player.open_file(filename[1])



class Thread():
    def __init__(self):
        ser = serial.Serial("/dev/ttyUSB0", 115200,timeout=0.1)  # timeout 단위: s
        self.modbus = pyModbus(ser)
        self.player = Player()

        #Get file_list and set the parameter
        self.file_list = os.listdir("./videos")
        self.file_list.sort()
        self.length = len(self.file_list)
        for i in range(0, self.length):
            self.file_list[i] = "./videos/" + self.file_list[i]
        self.play_request_flag = [0 for _ in range(0, self.length)]

        # Play init File
        self.player.open_file(self.file_list[0])

        # # Add to listener
        self.listener()


    def listener(self):
        """Confirm the plc status
        """
        # Listen to PLC
        self.play_request = self.modbus.readCoilStatus(1, 0, self.length)
        self.playing = self.modbus.readCoilStatus(1,100,1)

        #if Listen result is
        for i in range(0, self.length):
            if self.play_request[i] is 0:
                self.play_request_flag[i] = 0

            elif self.play_request[i] is 1 and self.play_request_flag[i] is 0:
                self.modbus.writeSingleCoil(1,i,False)
                self.player.open_file(self.file_list[i])
                self.play_request_flag[i] = 1

        if self.playing[0] is 1:
            self.player.play_only()
        else:
            self.player.pause_only()

        threading.Timer(0.1, self.listener).start()

def main():
    thread = Thread()
    input()

if __name__ == '__main__':
    main()
