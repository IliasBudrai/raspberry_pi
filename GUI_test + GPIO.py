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
            if (s1.get() - s2.get()) >= 0:
                time.sleep((s1.get() - s2.get())/1000)
            if start_statu[0]:
                ca.itemconfig(ItemIds[0], fill="yellow")
                GPIO.output(3, True)
            time.sleep(s2.get()/1000)
        
def f3():
    x = 250
    while True:
        
        if start_statu[0]:
            if ca.itemcget(ItemIds[0], "fill") == "black":
                if x > 240:
                    x = x - s3.get()
            else:
                if x < 290:
                    x = x + s3.get()
            ca.coords(ItemIds[2], x-50, 100-10, x+60, 100+10)
            time.sleep(0.002)

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
s1.set(1000)

s2 = Scale(root, from_=1, to=1000, orient=HORIZONTAL, label='percage')
s2.grid(row=2, column=0)
s2.set(200)


s3 = Scale(root, from_=1, to=20, orient=HORIZONTAL, label='vitesse/pression')
s3.grid(row=3, column=0)



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
ItemIds[1]=ca.create_rectangle(200-20, 100-20, 200+50, 100+20)

x = 250
ItemIds[2]=ca.create_rectangle(x-50, 100-10, x+60, 100+10, fill="blue")

ItemIds[3]=ca.create_rectangle(330 - 2, 100-30, 330 + 2, 100+30, fill="white")




t2 = threading.Thread(target=f2)
t3 = threading.Thread(target=f3)
t2.start()
t3.start()

b1.bind("<Button-1>", f4)
b2.bind("<Button-1>", f5)


root.mainloop()
                            







