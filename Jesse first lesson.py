
# priceofeachitem= int(input("what is the price of each of the items"))
# itemone= int(input("price of item1"))
# itemtwo= int(input("price of item2"))
# itemthree= int(input("price of item3"))
# itemfour= int(input("price of item4"))
# itemfive= int(input("price of item5"))
# print(itemone+itemtwo+itemthree+itemfour+i
import tkinter as jesse
from tkinter import messagebox

mainwindow=jesse.Tk()
mainwindow.geometry("900x400")
mainwindow.configure(bg="pink")

labelone= jesse.Label(text="Enter a value in pounds", font=("serif",36))
labelone.grid(row=0, column=0)

entryone= jesse.Entry(font=("Algerian", 15))
entryone.grid(row=0, column=1)
def converter():
    poundvalue=float(entryone.get())
    kilogramvalue= poundvalue * 0.454
    messagebox.showinfo("the conversion is:",kilogramvalue)

buttonone=jesse.Button(text="Convert to kilograms", font=("Serif", 30), command=converter)
buttonone.grid(row=1,column=1)
mainwindow.mainloop()
