from tkinter import *
import trace
import threading
import time

def clicker2():
    for i in range(1000):
        ca.itemconfig(ItemIds[0], fill="black")
        time.sleep((s1.get() - s2.get())/1000)
        ca.itemconfig(ItemIds[0], fill="yellow")
        time.sleep(s2.get()/1000)
        


    
        

root = Tk()

ca = Canvas(root, width=400, height=300, background="grey")
ca.grid(row=3, column=0, columnspan=2)

ItemIds=[None,None]

ItemIds[0]=ca.create_oval(100-10, 100-10, 100+10, 100+10, width=2, fill="yellow")


s1 = Scale(root, from_=200, to=1000, orient=HORIZONTAL, label='distance')
s1.grid(row=1, column=0, columnspan=2)

s2 = Scale(root, from_=50, to=200, orient=HORIZONTAL, label='percage')
s2.grid(row=2, column=0, columnspan=2)


ItemIds=[None,None]

ItemIds[0]=ca.create_oval(100-10, 100-10, 100+10, 100+10, width=2, fill="yellow")





t2 = threading.Thread(target=clicker2)
t2.start()


root.mainloop()
                            







