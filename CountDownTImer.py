import time


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs) #02d meaning an integer (d) with a min width 2 with 0 padding on the left
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time is Over!")
    


t = input ("Enter the time in seconds: ")

countdown(int(t))