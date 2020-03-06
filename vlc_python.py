import vlc

class VLC():
    def __init__(self):
        self._instance = vlc.Instance(['--video-on-top', '--input-repeat=-1'])
        self._player = self._instance.media_player_new()
        self._player.set_fullscreen(False)
        self.pre_playing = 1
        self.playing = 1
        self.playable = 0
        # self.pre_video

    def play(self, path):
        media = self._instance.media_new(path)
        self._player.set_media(media)
        self._player.play()

    def resume(self):
        if self.playing is 0:
            self._player.play()
            self.playing = 1

    def changePlaying(self):
        if self.pre_playing is self.playing:
            return False
        else:
            self.pre_playing = self.playing
            return True
        # def changeVideo(self):
        #

    def pause(self):
        if self.playing is 1:
            vlc.libvlc_media_player_set_pause(self._player, 1)
            self.playing = 0
