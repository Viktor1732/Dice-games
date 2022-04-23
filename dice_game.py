from tkinter import *


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
root.mainloop()