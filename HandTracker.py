import time
from PIL import Image

countdownsec = 0

print("Please schedule a good time for us to begin our stretch session:")
time_hourmin = input("When would you like to schedule our next session?:")
time_hourmin = time(time_hourmin)

def countdown60(countdownsec):


    seconds = 60

    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")

    time.sleep(1)
    print("Time is up")

def countdown30(countdownsec):


    seconds = 30

    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")

    time.sleep(1)
    print("Time is up")

def countdown15(countdownsec):


    seconds = 15

    for i in range(seconds):
        print(str(seconds-i) + " seconds remaining \n")

    time.sleep(1)
    print("Time is up")



def warm_up():
    warmup_repeat = 0

    if warmup_repeat <= 4:
        print("Please perform a warm-up before we begin:")
        im = Image.open("ctwarmup.webp")
        im.show()
        countdown15(countdownsec)
    else:
        print("Please schedule a good time for us to begin our stretch session:")
        time_hourmin = input("When would you like to schedule our next session?:")
        time_hourmin = time(time_hourmin)
    

def scheduled_stretch():
    flex_repeat = 0
    extend_repeat = 0

    if  flex_repeat <= 4:
     print("Please complete a Wrist flexor stretch:")
     im2 = Image.open("ctwristflexorstretch.jpeg")
     im2.show()
     countdown60(countdownsec)
     countdown15(countdownsec)
     flex_repeat += 1
    if extend_repeat <= 4:
     print("Please complete a Wrist extensor stretch:")
     im3 = Image.open("ctwristextensorstretch.jpeg")
     im3.show()
     countdown60(countdownsec)
     countdown15(countdownsec)
     extend_repeat += 4

