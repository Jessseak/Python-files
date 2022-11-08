import tkinter as Jesse
from tkinter import messagebox

mainwindow=Jesse.Tk()
mainwindow.geometry="1600x900"
mainwindow.configure(bg="green")

labelone= Jesse.Label(text="What country were you born?", font=("Algerian",36))
labelone.grid(row=0, column=0)

entryone= Jesse.Entry(font=("serif", 25))
entryone.grid(row=0, column=1)
def converter():
    placeofbirth= (entryone.get())
    answer= placeofbirth.upper()
    messagebox.showinfo("Your place of birth is :",answer)

buttonone=Jesse.Button(text="This is your place of birth", font=("Serif", 30), command=converter)
buttonone.grid(row=1,column=1)

mainwindow.mainloop()

#studentnames= ['nifemi','jessica'],['batul','jesse'],['jinki','ojie']
#print(studentnames[2],[1])

