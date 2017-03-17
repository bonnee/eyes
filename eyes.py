#!/usr/bin/env python3

import os
import json
import i3ipc

cmd = 'ffplay -fflags nobuffer -an -framedrop -fast rtsp://'
#cmd='mplayer --nosound --dr --framedrop --nocache --quiet --fps=5 rtsp://'
with open('streams.json') as data_file:    
    streams = json.load(data_file)

#streams = ['192.168.1.120/live2.sdp', '192.168.1.121/live2.sdp', '192.168.1.122/live2.sdp', '192.168.1.187/live2.sdp']

for stream in streams:
  os.system(cmd+stream + " & > /dev/null")

i3 = i3ipc.Connection()

