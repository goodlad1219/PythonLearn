import time
import os

def convert(t):
    return t * 60

def countdown(t, label):
    # 60
    while t:
        min,sec = divmod(t, 60)
        print(f"{label}:{min:02d}:{sec:02d}",end="\r")
        time.sleep(1)
        t -= 1

def pomodoro(work, rest):
    #convert min to sec
    w = convert(work)
    r = convert(rest)
    countdown(w, "Work")
    os.system("cls")
    countdown(r, "Rest")
    os.system("cls")

work = int(input("Work time (min): "))
rest = int(input("Rest time (min): "))
1
pomodoro(work, rest)