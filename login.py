from tkinter import *
import os
import pymysql

root=Tk()
root.title("Login Window")
root.config(bg='tan')
root.geometry('1000x600')
root.resizable(0,0)

#FRAME AND BACKGROUND PICTURE
frame=Frame(root,width=500,height=400)
frame.place(x=0,y=0)
frame.config()
photo=PhotoImage(file="C:\\Users\\prabhu\\Downloads\\OSTL PROJECT\\wall.gif")
label = Label(root,image = photo)
label.image = photo # keep a reference!
label.grid(row=0,column=0,columnspan=20,rowspan=20)

"""photo_1=PhotoImage(file="C:\\Users\\sushant\\Desktop\\OSTL PROJECT\\this\\wall1.gif")
label=Label(root,image=photo_1,text='WELCOME TO PHONE DIRECTORY',font=('Calibri ',20),fg="black")
label.place(x=270,y=50)"""

def user_pass():
    if (((usern.get()=='sushant') and (passwd.get()=='1234')) or ((usern.get()=='suraj') and (passwd.get()=='prabhu')) or ((usern.get()=='swapnil') and (passwd.get()=='patil'))):
        root.destroy()
        from phonebook import phonebook
    elif usern.get()=='':
        message=Label(text='Please enter your Username',font=('Calibri ',15),bg='tan')
        message.place(x=340,y=380)
    elif passwd.get()=='':
        message=Label(text='Please enter your Password',font=('Calibri ',15),bg='tan')
        message.place(x=340,y=380)
    elif usern.get()=='' and passwd.get()=='':
        message=Label(text='Please enter your Username and Password',font=('Calibri ',15),bg='tan')
        message.place(x=340,y=380)
    else:
        message=Label(text='Incorrect username or password ',font=('Calibri ',15),bg='tan')
        message.place(x=340,y=380)

l1 = Label(root,text="Username :",font=('Calibri ',15),bg='tan')
l1.place(x=300,y=200)
usern=StringVar()
e=Entry(root,textvariable=usern,font=('Calibri ',15),bd=1,bg='burlywood')
e.place(x=415,y=200)
e.focus()

l2 = Label(root,text="Password :",font=('Calibri ',15),bg='tan')
l2.place(x=300,y=250)
passwd=StringVar()
e1=Entry(root,show='*',textvariable=passwd,font=('Calibri ',15),bg='burlywood')
e1.place(x=415,y=250)

b=Button(root,text="LOGIN",font=('Calibri ',15),command=user_pass,bg='ivory')
b.place(x=430,y=300)

root.mainloop()
