import subprocess
import vlc
import time
import random as r
from datetime import datetime, timedelta

print(datetime.now() + timedelta(minutes=1))


def vlc_setup(path):
    inst = vlc.Instance()

    media_list = inst.media_list_new()

    player = inst.media_list_player_new()

    # player.set_fullscreen(True)

    media = inst.media_new_path(path)

    media_list.add_media(media)

    player.set_media_list(media_list)

    # inst.vlm_set_loop(path, True)
    player.set_playback_mode(vlc.PlaybackMode.loop)

    new = inst.media_player_new()

    new.set_fullscreen(True)

    player.set_media_player(new)

    return player

player = vlc_setup("/home/tobi/Videos/test.mp4")

# set pause if do pause is 1, play is do pause 0
player.play()
# player.set_pause(do_pause=1)
# player.set_time(0)

while True:
    pass


# while True:
#     nr = r.randint(1, 5)
#     print(nr)
    
#     time.sleep(2)

#     # keyboard.on_press_key("l", play_video)
#     if nr == 3:
#         player.play()
#         time.sleep(31)
#         player.set_pause(do_pause=1)
    

