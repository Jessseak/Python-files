#list=[2,3,4,5,6,7]
#for number in list:
   # if number %2 ==0:
      #  print(number)

#write a program to get the name of a user using the input function and append the name to an empty list
#solution:
#name= input('what is your name?')
#emptylist=[]
#emptylist.append(name)
#print(emptylist)

#print the last element of the list: ['nigeria','ghana','sierra leone']
#countries=['nigeria','ghana','sierra leone']
#print(countries[2])

import tkinter as Jesse
from tkinter import messagebox

mainwindow=Jesse.Tk()
mainwindow.geometry("1800x1000")
mainwindow.configure(bg='purple')

firstlabel = Jesse.Label(text="confirm your password", font=('Arial',32))
firstlabel.grid(row=0, column=0)
def confirmpassword
    takenpassword= ['abc123','def123','emma']
    firstentry=userentry.get()
    if userentry in takenpassword:
        messagebox.showinfo(text='password is taken',firstentry)
    else:

        messagebox.showinfo(text='password is available',firstentry)

userentry = Jesse.Entry(font=('Arial',23))
userentry.grid(row=0, column=1)

userbutton=Jesse.Button(text='confirm password', font=('serif',28),command=confirmpassword))
userbutton.grid(pady=5)

mainwindow.mainloop()

