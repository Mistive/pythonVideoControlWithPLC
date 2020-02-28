#-*- coding:utf-8 -*
#https://www.videolan.org/developers/vlc/doc/doxygen/html/group__libvlc__video.html#gabdbb7230cc3db78e73070ce10e679315

# import vlc
# import time
#
# player = vlc.MediaPlayer("./videos/01.mp4")
#
# vlc.libvlc_set_fullscreen(player, True)
# player.play()
#
# time.sleep(3)
#
# player2 = vlc.MediaPlayer("./videos/02.mp4")
# vlc.libvlc_set_fullscreen(player2, True)
# player.stop(), player2.play()
# time.sleep(3)
# player.play()
# time.sleep(5)

import vlc
import time
class Player():
    def __init__(self):
        self._instance = vlc.Instance(['--video-on-top', '--input-repeat=-1'])
        self._player = self._instance.media_player_new()
        self._player.set_fullscreen(True)

    def play(self, path):
        media = self._instance.media_new(path)
        self._player.set_media(media)
        self._player.play()

    def stop(self):
        self._player.stop()

# p=Player()
# p.play('./videos/01.mp4')
# time.sleep(5)
# p.stop()
# p.play('./videos/02.mp4')
# time.sleep(5)