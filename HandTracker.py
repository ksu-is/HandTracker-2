import time

print("Hello, welcome to HandTracker! \n")
print("Please schedule a good time for us to begin our stretch session:")
time_hourmin = time(time_hourmin)

time_hrmn = ""

def warm_up(time_hrmn):
    warmup_repeat = 0

    if warmup_repeat <= 4:
        print("Please perform a warm-up before we begin:")
        image: ctwarmup.webp
        countdown(30sec)
    else:
        print("Please schedule a good time for us to begin our stretch session:")
        time_hourmin = time(time_hourmin)
    

def scheduled_stretch(time_hrmn):
    flex_repeat = 0
    extend_repeat = 0

while True:
    if  flex_repeat <= 4:
     print("Please complete a Wrist flexor stretch:")
     image: ctwristflexorstretch.jpeg
     countdown(30 sec)
     rest(15 sec)
     flex_repeat += 1
    if extend_repeat <= 4:
     print("Please complete a Wrist extensor stretch:")
     image: ctwristextensorstretch.jpeg
     countdown(30 sec) 
     rest(15 sec)
     extend_repeat += 4



