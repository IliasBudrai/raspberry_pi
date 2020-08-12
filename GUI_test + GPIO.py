from tkinter import *
import RPi.GPIO as GPIO
import threading
import time

def f2():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    while True:
        if start_statu[0]:
            ca.itemconfig(ItemIds[0], fill="black")
            GPIO.output(3, False)
            time.sleep(s1.get()/1000)
        if start_statu[0]:
             ca.itemconfig(ItemIds[0], fill="yellow")
             GPIO.output(3, True)
             time.sleep(s2.get()/10000)
        


def f4(event):
    start_statu[0] = True
    print("statu on")

def f5(event):
    start_statu[0] = False
    ca.itemconfig(ItemIds[0], fill="black")
    print("statu off")

root = Tk()

s1 = Scale(root, from_=1, to=3000, orient=HORIZONTAL, label='distance')
s1.grid(row=1, column=0)
s1.set(410)

s2 = Scale(root, from_=300, to=400, orient=HORIZONTAL, label='percage')
s2.grid(row=2, column=0)
s2.set(350)

start_statu=[None for _ in range(1)]
start_statu[0] = False

b1 = Button(root, text="Start", fg="green")
b1.grid(row=2, column=1)

b2 = Button(root, text="STOP", fg="red")
b2.grid(row=3, column=1)


ca = Canvas(root, width=400, height=300, background="grey")
ca.grid(row=4, column=0, columnspan=2)


ItemIds=[None for _ in range(6)]

ItemIds[0]=ca.create_oval(100-10, 100-10, 100+10, 100+10, width=2, fill="black")

t2 = threading.Thread(target=f2)

t2.start()


b1.bind("<Button-1>", f4)
b2.bind("<Button-1>", f5)


root.mainloop()
                            








