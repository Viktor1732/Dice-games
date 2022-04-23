import random
import time
from tkinter import *


def brosok():
    random_cube = random.choice(
        ['b.png', 'b2.png', 'b3.png', 'b4.png', 'b5.png', 'b6.png']
    )
    return random_cube

def img(event):
    global cube1, cube2
    for i in range(10):
        cube1 = PhotoImage(file=(brosok()))
        cube2 = PhotoImage(file=(brosok()))
        lab1['image'] = cube1
        lab2['image'] = cube2
        root.update()
        time.sleep(0.12)

root = Tk()
root.title('Dice game! Make a throw!')
root.geometry('400x200')
root.iconphoto(True, PhotoImage(file=('iconka.png')))
root.resizable(width=False, height=False)
holst = PhotoImage(file=('holst.png'))
Label(root, image=holst).pack()
lab1 = Label(root)
lab2 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<1>', img)
img('event')
root.mainloop()
