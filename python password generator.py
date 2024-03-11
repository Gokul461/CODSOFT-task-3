import random
from tkinter import *
import string
import tkinter.messagebox 
import pyperclip

def generate():
    small = string.ascii_lowercase
    big = string.ascii_uppercase
    p = string.punctuation
    num = string.digits
    midpass = small+num+big
    strongpass = small+big+num+p
    l = int(spin.get())
    if choice.get()==0:
        tkinter.messagebox.showwarning(title="Warning!",message="Please click any type of password")
    elif choice.get() == 1:
        delete()
        password = random.sample(strongpass,l)
        entry.insert(0,password)
    elif choice.get() == 2:
        delete()
        password = random.sample(midpass,l)
        entry.insert(0,password)
    elif choice.get() == 3:
        delete()
        password = random.sample(small,l)
        entry.insert(0,password)

def copy():
    password=entry.get()
    password = str(password)
    word = password.replace(" ","")
    pyperclip.copy(word)

def delete():
    content = entry.get()
    entry.delete(0,END)

root = Tk()
root.geometry("300x500")
root.title("Password generator")
root.resizable(False,False)
root.config(bg='light blue')

head = Label(text="Password Generator",font=('Copperplate Gothic Bold',16),background='dark blue',width=10,height=2,fg='white')
head.pack(fill=X)
enter_lab = Label(text='Select the type of password',bg='light blue',font=("Arial black",10))
enter_lab.pack(pady=10,fill=X)

choice = IntVar()
style = ('Aptos Display',12)
strong = Radiobutton(root,text="Strong",variable=choice,value=1,width=11,font=style)
moderate = Radiobutton(root,text="Medium",variable=choice,value=2,width=11,font=style)
week = Radiobutton(root,text="Week",variable=choice,value=3,width=11,font=style)
strong.pack(pady=3,padx=3)
moderate.pack(pady=3,padx=3)
week.pack(pady=3,padx=3)

length_lab = Label(text='Password length',bg='light blue',font=("Arial black",10))
length_lab.pack(pady=10,fill=X)
spin = Spinbox(root,from_=5,to=10,width=9)
spin.pack(pady=6)

generate_but = Button(root,text='Generate',font = style,fg='white',bg='gray20',width=15,command= lambda:generate())
generate_but.pack(padx=5,pady=10)
entry = Entry(root,width=30,border=4)
entry.pack(pady=10,padx=5)

copy_but = Button(root,text='Copy',font = style,width=11,fg='white',bg='grey20',command=copy)
copy_but.pack(padx=5,pady=10)

reset_but = Button(root,text='Reset',font = style,width=11,fg='white',bg='grey20',command = lambda:delete())
reset_but.pack(padx=5,pady=10)

root.mainloop()