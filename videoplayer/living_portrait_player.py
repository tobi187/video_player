from gpiozero import MotionSensor
from omxplayer.player import OMXPlayer
from datetime import datetime, timedelta
import subprocess
from time import sleep
import json
from threading import Thread
from random import randint

with open("config.json", "r") as f:
    configs = json.load(f)


def thread2_func():
    sleep(10)


thread2 = Thread(target=thread2_func)


def thread1_func():
    while True:
        nr = randint(1, 5)
        sleep(2)
        if nr == 3:
            thread2.run()
            sleep(5)


thread1 = Thread(target=thread1_func)


end = datetime.now() + timedelta(minutes=configs["duration"])

try:
    file = configs["video_name"]
    player = OMXPlayer(file,  args=['--no-osd', '--loop'])
    # pir = MotionSensor(4)
    # player.play()
    player.set_position(configs["start"])
    # player.pause()
    sleep(1)
    while True:
        player.pause()
        if datetime.now() < end:
            player.quit()
            kill = ["killall", "omxplayer"]
            subprocess.run(kill)
            # command = ["shutdown", "-P", "now"]
            # subprocess.run(command)
            subprocess.run(["echo", "done"])
            sleep(2)
            exit()
        # if pir.motion_detected:
        if thread2.is_alive():
            player.play()
            if configs["video_duration"] == "":
                sleep(player.duration())
            else:
                sleep(configs["video_duration"])
        else:
            pass
        player.set_position(configs["start"])


except KeyboardInterrupt:
    kill = ["killall", "omxplayer"]
    subprocess.run(kill)
    sleep(3)
    exit()
