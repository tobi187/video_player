import vlc
import time
from datetime import datetime, timedelta
import subprocess
import random as r
from threading import Thread

# shutdown_rdy = False
end = datetime.now() + timedelta(minutes=3)


# def shutdown():
#     counter = 0
#     while counter < 3:
#         time.sleep(30)
#         counter += 1
    
#     while True:
#         if shutdown_rdy:
#             time.sleep(10)
#             if shutdown_rdy:
#                 exit()


# thread = Thread(target=shutdown)
# thread.start()

# thread2 = Thread(target=bgpic)
# thread2.start()


# thread = Process(target=shutdown)
# thread.start()


# + minutes till power off
# subprocess.run(["shutdown", "-P", "+2"])


def play_video():
    inst = vlc.Instance()

    player = inst.media_player_new()

    player.set_fullscreen(True)

    media_list = inst.media_list_new()

    media = inst.media_new_path("/home/tobi/Videos/test.mp4")

    media_list.add_media(media)

    list_player = inst.media_list_player_new()

    list_player.set_media_list(media_list)

    list_player.set_playback_mode(vlc.PlaybackMode.loop)

    list_player.set_media_player(player)

    return list_player

player = play_video()
player.play()
player.set_pause(do_pause=1)


while True:
    nr = r.randint(1, 3)
    print(nr)
    
    if end < datetime.now():
        exit()


    # keyboard.on_press_key("l", play_video)
    if nr == 3:
        # shutdown_rdy = False
        player.set_pause(do_pause=0)
    else:
        player.set_pause(do_pause=1)
    
    time.sleep(10)
    
    # shutdown_rdy = True

    


