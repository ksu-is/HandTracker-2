import vlc
import os
import time

from PIL import Image
from os import *

p = vlc.MediaPlayer("Announcement sound effect.mp3")
p_rest = vlc.MediaPlayer('WarmUpStart.mp3')

current_time = time.strftime("%H:%M")

t = time.strptime(current_time, "%H:%M")
timevalue_12hour = time.strftime( "%I:%M %p", t )



countdownsec = 0


returning_user_check = input("Would you like a refresher on how to perform wrist stretches? (Yes or No):")

print("The current time is", timevalue_12hour)

time_hourmin = input('Please provide 4 times of day you would like to schedule your sessions: (Ex: 09:30 PM,01:00 PM)')
time_hourmin = time_hourmin.split(",")

print("Your 4 stretches will take place at" ,time_hourmin, " today.")


print(time_hourmin[0])

def startfile(fn):
    os.system('open %s' % fn)

    

def warmupvideotimer(countdownsec):
    print("Please take some time to perform a few warm-ups before your stretch session:")
    p.play()
    seconds = 115
    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    p.stop()
    print("Time is up")


def tendonglidevideotimer(countdownsec):
    seconds = 35
    p.play()
    print("Please watch the following video on how to perform a tendon glide.")
    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    p.stop()
    print("Time is up")

def countdown60(countdownsec):
    p.play()
    seconds = 60

    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    p.stop()
    print("Time is up")

def countdown15rest(countdownsec):

    p_rest.play()
    seconds = 15
    print("Please allow your wrist to rest for 15 seconds.")

    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    p_rest.stop()
    print("The resting period has ended.")

def countdown45(countdownsec):
    p.play()
    seconds = 45
    
    
    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")
        time.sleep(1)
    p.stop()
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

     print("Please complete a Wrist flexor stretch:")
     os.system('open WristFlexorStretchVid.mp4')
     countdown45(countdownsec)
     countdown15rest(countdownsec)


def scheduled_extensor(countdownsec):

     print("Please complete a Wrist extensor stretch:")
     os.system('open WristExtensorStretchVid.mp4')
     countdown45(countdownsec)
     countdown15rest(countdownsec)


def scheduled_tendonglide(countdownsec):

     print("Please complete a series of Tendon glides:")
     os.system('open TendonGlidesExercise.mp4')
     tendonglidevideotimer(countdownsec)
     countdown45(countdownsec)
     countdown15rest(countdownsec)


def novid_warm_up(countdownsec):
    warmup_repeat = 0

    if warmup_repeat <= 4:
        print("Please perform a warm-up before we begin:")
        warmupvideotimer(countdownsec)
        countdown15rest(countdownsec)
    else:
        print("Please schedule a good time for us to begin our stretch session:")
        time_hourmin = input("When would you like to schedule our next session?:")
        time_hourmin = time(time_hourmin)
    

def novid_scheduled_flexor(countdownsec):

     print("Please complete a Wrist flexor stretch:")
     countdown45(countdownsec)
     countdown15rest(countdownsec)

def novid_scheduled_extensor(countdownsec):

     print("Please complete a Wrist extensor stretch:")
     countdown45(countdownsec)
     countdown15rest(countdownsec)


def novid_scheduled_tendonglide(countdownsec):

     print("Please complete a series of 20 Tendon glides:")
     countdown45(countdownsec)
     countdown15rest(countdownsec)




while returning_user_check.lower() == 'yes':
    rep = 0
    if time_hourmin[0] == timevalue_12hour:
            warm_up(countdownsec)
            if rep == 0:
                warm_up(countdownsec)
                scheduled_flexor(countdownsec)
                scheduled_extensor(countdownsec)
                scheduled_tendonglide(countdownsec)
                rep += 1
                time_hourmin[0] = 'null'
            else:
                print("Your stretching session is now over. Until next time!")
                break


    elif time_hourmin[1] == timevalue_12hour:

            if rep == 1:
                warm_up(countdownsec)
                scheduled_tendonglide(countdownsec)
                scheduled_flexor(countdownsec)
                scheduled_extensor(countdownsec)
                rep += 1
                time_hourmin[1] = 'null'
            else:
                print("Your stretching session is now over. Until next time!")
                break 

    elif time_hourmin[2] == timevalue_12hour:
            if rep == 2:
                warmupvideotimer(countdownsec)
                novid_scheduled_extensor(countdownsec)
                novid_scheduled_tendonglide(countdownsec)
                novid_scheduled_flexor(countdownsec)
                rep += 1
                time_hourmin[2] = 'null'
            else:
                print("Your stretching session is now over. Until next time!")
                break       

    elif time_hourmin[3] == timevalue_12hour:
            if rep == 3:
                scheduled_flexor(countdownsec)
                scheduled_extensor(countdownsec)
                scheduled_tendonglide(countdownsec)
                rep += 1
                time_hourmin[3] = 'null'
            else:
                print("Your stretching session is now over. Until next time!")
                break
    else:
            print("Your stretching session is now over. Until next time!")
            break

while returning_user_check.lower() == 'no':

          rep = 0
          if time_hourmin[0] == timevalue_12hour:
            if rep == 0:
                print("Please perform a warm-up before we begin:")
                warmupvideotimer(countdownsec)
                novid_scheduled_flexor(countdownsec)
                novid_scheduled_extensor(countdownsec)
                novid_scheduled_tendonglide(countdownsec)
                rep += 1
                time_hourmin[0] = 'null'
            else:
                print("Your stretching session is now over. Until next time!")
                break

          elif time_hourmin[1] == timevalue_12hour:
            print("Please perform a warm-up before we begin:")
            warmupvideotimer(countdownsec)
            if rep == 1:
                novid_scheduled_tendonglide(countdownsec)
                novid_scheduled_flexor(countdownsec)
                novid_scheduled_extensor(countdownsec)
                rep += 1
                time_hourmin[1] = 'null'
            else:
                print("Your stretching session is now over. Until next time!")
                break

          elif time_hourmin[2] == timevalue_12hour:
            print("Please perform a warm-up before we begin:")
            warmupvideotimer(countdownsec)
            if rep == 2:
                novid_scheduled_flexor(countdownsec)
                novid_scheduled_tendonglide(countdownsec)
                novid_scheduled_extensor(countdownsec)
                rep += 1
                time_hourmin[2] = 'null'
            else:
                print("Your stretching session is now over. Until next time!")
                break

          elif time_hourmin[3] == timevalue_12hour:
            print("Please perform a warm-up before we begin:")
            warmupvideotimer(countdownsec)
            if rep == 3:
                novid_scheduled_extensor(countdownsec)
                novid_scheduled_flexor(countdownsec)
                novid_scheduled_tendonglide(countdownsec)
                rep += 1
                time_hourmin[3] = 'null'
            else:
                print("Your stretching session is now over. Until next time!")
                break


          else:
            print("Your stretching session is now over. Until next time!")
            break

