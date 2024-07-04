import time
from tkinter import *

FONT = ("Aeriel",30)

def countdown(t):
    while t:
        min,sec = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min,sec)
        label_3.config(text=timer)
        window.update()
        time.sleep(1)
        t -= 1
    label_3.config(text="Time is done")

def time_select():
    t = entry_1.get()
    try:
        countdown(int(t))
    except ValueError:
        label_3.config(text="Invalid input. Please enter an integer.")

window = Tk()
window.config(width=200,height=200)
window.title("Countdown Timer")

label_1 = Label(window)
label_1.config(padx=15,pady=15,font=FONT,text="Countdown Timer")
label_1.pack()

label_2 = Label(window)
label_2.config(padx=15,pady=15,text="Please !! Enter the time")
label_2.pack()

entry_1 = Entry(window)
entry_1.pack()

button_1 = Button(window,text="Countdown!!",command=time_select)
button_1.pack()

label_3 = Label(window,padx=15,pady=15)
label_3.pack()

window.mainloop()

