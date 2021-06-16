#!/bin/bash

echo "Bitte gib den Speicherort des Scripts (living_portrait_player.py) an"

read -r location

DIR="/home/pi/.config/autostart/"

echo "$location $DIR"

#if [ -d "$DIR" ]; then
#  mv "$location" "$DIR"
#else
#  mkdir "/home/pi/.config/autostart"
#  mv "$location" "$DIR"
#fi
