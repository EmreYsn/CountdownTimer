import time

def countdown(t):
    while t:
        min,sec = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min,sec)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1

    print("time is done.")

t = input("Enter the time:")

countdown(int(t))