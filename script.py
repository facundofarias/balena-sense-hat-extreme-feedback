import os
import time
import json
import urllib.request

from sense_hat import SenseHat

interval = 10
username = os.environ['BITBUCKET_USERNAME']
repository = os.environ['BITBUCKET_REPOSITORY']

sense = SenseHat()
sense.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
    
def red_cross():
    R = red
    O = nothing
    logo = [
    R, R, O, O, O, O, R, R,
    R, R, R, O, O, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    O, O, R, R, R, R, O, O,
    O, R, R, R, R, R, R, O,
    R, R, R, O, O, R, R, R,
    R, R, O, O, O, O, R, R,
    ]
    return logo
    
def green_plus():
    G = green
    O = nothing
    logo = [
    O, O, O, G, G, O, O, O, 
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O, 
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    O, O, O, G, G, O, O, O,
    ]
    return logo

images = [red_cross, green_plus]
count = 0

while True:
    time.sleep(interval)
    url = 'https://api.bitbucket.org/2.0/repositories/%s/%s/pipelines/?sort=-created_on' % (username, repository)
    contents = urllib.request.urlopen(url).read()
    json_content = json.loads(contents.decode('utf-8'))
    last_build = json_content['values'].pop()
    if last_build['state']['name'] == 'COMPLETED' and last_build['state']['result']['name'] == 'SUCCESSFUL':
      # Do something
      print ('GREEN')
      sense.set_pixels(green_plus())
    else:
      # Do something else
      print ('RED')
      sense.set_pixels(red_cross())