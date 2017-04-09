#!/usr/bin/python

import os
import sys
import thread
import time
import json

def launch(addr):
  #cmd='mplayer --nosound --dr --framedrop --nocache --quiet --fps=5 '
  cmd = 'ffplay -fflags nobuffer -an -framedrop -loglevel error -fast -threads 2 -async 1 -preset ultrafast -tune zerolatency -vf scale=640:-1 '
  os.system(cmd+addr)

def start():
  with open('streams.json') as data_file:
      streams = json.load(data_file)
  
  print "Starting up streams. Don't change workspace until all streams appear."
  time.sleep(8)

  for stream in streams:
    #launch(stream)
    thread.start_new_thread(launch, (stream,))
    time.sleep(2.5);

def full(mark):
  return mark

def mode(num):
  with open('modes.json') as data_file:
      modes = json.JSONDecoder().decode(data_file.read())
  return num

def halp():
  print 'Help:\ncoming soon'
  
print 'eyes.py v0.01a\n'

if len(sys.argv) > 1:
  a = sys.argv[1]

  if a == 'start':
    start()
  elif a == 'mode':
    mode(sys.argv[2])
  elif a == 'full':
    full(sys.argv[2])
  else:
    halp()
else:
  halp()
