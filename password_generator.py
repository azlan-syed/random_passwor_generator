from tkinter import *
import random
import string


def gen():
    password= []
    for i in range(4):
        lower=random.choice(string.ascii_lowercase)
        upper=random.choice(string.ascii_uppercase)
        password.append(lower)
        password.append(upper)
        passs=" ".join(str(x)for x in password)
        label.config(text=passs)

root =Tk()
label = Label(root, font = ('arial', 40, 'bold'))
label.pack()
button1 =Button(root,text="Generate", font = ('arial', 40, 'bold'),command= gen). place(x=100,y=200)                       
root.geometry("500x500")
root.title("password ")
root.mainloop()