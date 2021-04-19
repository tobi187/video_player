from player import Player
from datetime import datetime, timedelta
import random as r
from time import sleep
import subprocess
from omxplayer import OMXPlayer
from gpiozero import MotionSensor

end = datetime.now() + timedelta(minutes=10)

try:
    player = OMXPlayer("/home/pi/Videos/deep_end.mp4", args=["-o", "local", "--win", "0,0,640,480", "--loop", "--no-osd"])
    pir = MotionSensor(4)
    sleep(1)
    player.pause()
    player.set_position(0.0)
    should_stop = False
    while True:
        nr = r.randint(1, 3)
        print(nr)
        
        # if pir.motion_detected:
        if nr == 2:
            player.play()
            sleep(10)
            player.set_position(0.0)
            sleep(.5)
            player.pause()
            sleep(5)

        if datetime.now() > end:
            player.quit()
            subprocess.Popen(["shutdown", "-P", "now"])
            exit()
        sleep(2)
            

except KeyboardInterrupt:
    player.quit()
    exit()

    