# student_names = open("C:\\Users\\jesse\\OneDrive\\Desktop","w")
# student_names.write("james\n")
# student_names.write("jesse\n")
# student_names.write("peter\n")
# student_names.close()

#\ means new line
# w means writes
# a means append so the data in the text file cant be changed rather it adds the values to the end of the list
# r means read

# student_names = open("C:\\Users\\jesse\\OneDrive\\Desktop\\newfile.txt","r")
# student_details= student_names.read()
# print(student_details)
# student_names.close()



# numberfile=open('C:\\Users\\jesse\\OneDrive\\Desktop\\numbers.txt','r')
# number= numberfile.read()
# print(number)
# numberfile.close()

# import tkinter as Jesse
# mainwindow= Jesse.Tk()
# mainwindow.geometry('1600x900')
# mainwindow.configure(bg='black')
#
# idnumber=Jesse.Label(text='what is your id number',font= ('algerian',36 ))
# idnumber.grid(row=0, column=0)
#
# idnumber= Jesse.Entry(font=('serif',36))
# idnumber.grid(row= 0, column= 1)
#
# firstname =Jesse.Label(text='What is your first name',font= ('serif',36 ))
# firstname.grid(row=1, column=0)
# firstname= Jesse.Entry(font=('sans-serif',36))
# firstname.grid(row= 1, column= 1)
#
# lastname =Jesse.Label(text='Enter your last name',font= ('serif',36 ))
# lastname.grid(row=2, column=0)
# lastname= Jesse.Entry(font=('sans-serif',36))
# lastname.grid(row= 2, column= 1)
#
# average_grade =Jesse.Label(text='What is your average grade',font= ('sans-serif',36 ))
# average_grade.grid(row=3, column=0)
# average_grade= Jesse.Entry(font=('sans-serif',36))
# average_grade.grid(row= 3, column= 1)
#
#
#
#
#
# mainwindow.mainloop()
golf=open('c:\\users\\jesse\\onedrive\\desktop\\golf.txt','w')
golf.write()

golf.close()

golf_scores= open("C:\\Users\\jesse\\OneDrive\\Desktop\\golf.txt",'r')
golf_players= golf_scores.read()
print(golf_players)
golf_scores.close()