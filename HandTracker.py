import vlc
import os
import time
from PIL import Image
from os import *

p = vlc.MediaPlayer("StretchMusic.mp3")
countdownsec = 0


print("Please schedule a good time for us to begin our stretch session:")
time_hourmin = input("When would you like to schedule our next session?:")

current_time = time.strftime("%H:%M")
print("The current time is", current_time)

def startfile(fn):
    os.system('open %s' % fn)

def warmupvideotimer(countdownsec):
    print("Please take some time to perform a few warm-ups before your stretch session:")
    seconds = 120
    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    print("Time is up")

def countdown60(countdownsec):

    seconds = 60

    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    print("Time is up")
def countdown15rest(countdownsec):


    seconds = 15
    print("Please allow your wrist to rest for 15 seconds.")

    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    p.stop()
    print("The resting period has ended.")

def countdown30(countdownsec):

    p.play()
    seconds = 30
    
    
    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    
    print("Time is up")



def warm_up(countdownsec):
    warmup_repeat = 0

    if warmup_repeat <= 4:
        print("Please perform a warm-up before we begin:")
        startfile('WarmUpTrim.mp4')
        warmupvideotimer(countdownsec)
        countdown15rest(countdownsec)
    else:
        print("Please schedule a good time for us to begin our stretch session:")
        time_hourmin = input("When would you like to schedule our next session?:")
        time_hourmin = time(time_hourmin)
    

def scheduled_flexor(countdownsec):
    flex_repeat = 0


    if  flex_repeat < 4:
     print("Please complete a Wrist flexor stretch:")
     os.system('open WristFlexorStretchVid.mp4')
     countdown30(countdownsec)
     countdown15rest(countdownsec)
     flex_repeat += 1

def scheduled_extensor(countdownsec):
    extend_repeat = 0
    
    if extend_repeat < 4:
     print("Please complete a Wrist extensor stretch:")
     os.system('open WristExtensorStretchVid.mp4')
     countdown30(countdownsec)
     countdown15rest(countdownsec)
     extend_repeat += 4

def scheduled_flexor(countdownsec):
    flex_repeat = 0


    if  flex_repeat < 4:
     print("Please complete a Wrist flexor stretch:")
     os.system('open WristFlexorStretchVid.mp4')
     countdown30(countdownsec)
     countdown15rest(countdownsec)
     flex_repeat += 1

rep = 0


while rep < 4:
    rep += 1
    if time_hourmin == time.strftime("%H:%M"):
        warm_up(countdownsec)
        if rep < 4:
            scheduled_flexor(countdownsec)
            scheduled_extensor(countdownsec)
            rep += 1
        else:
            print("Your stretching session is now over. Until next time!")
    else:
        print("Your stretching session is now over. Until next time!")

