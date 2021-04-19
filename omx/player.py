from omxplayer import OMXPlayer
from time import sleep

class Player:

    def __init__(self, path):
        self.path = path
        self.player = OMXPlayer(self.path, args=["--loop", "-o", "local", "--win", "0,0,640,480"])
        # self.player.play()
        # self.player.set_position(10.0)
        # self.player.pause()

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def toggle(self):
        self.player.play_pause()
    
    def reset(self):
        self.player.pause()
        self.player.set_position(0.0)

