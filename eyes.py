#!/usr/bin/env python3

import os
import time
import json
import i3ipc

cmd = 'ffplay -fflags nobuffer -an -framedrop -loglevel error -fast -threads 2 -async 1 -preset ultrafast -tune zerolatency -vf scale=640:-1 '
aft = ' &'
#cmd='mplayer --nosound --dr --framedrop --nocache --quiet --fps=5 '

with open('streams.json') as data_file:    
    streams = json.load(data_file)

os.system('i3-msg "workspace 1"')
os.system('i3-msg "append_layout $HOME/eyes/layout.json"')

for stream in streams:
  os.system(cmd+stream+aft)
  time.sleep(1.5);


i3 = i3ipc.Connection()

time.sleep(5)

tree = i3.get_tree().leaves()
for cam in tree:
  if(cam.workspace().name == '1'):
    print("Name: %s | Class: %s" % (cam.name, cam.window_class))

