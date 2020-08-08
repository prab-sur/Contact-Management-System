from tkinter import *
from tkinter import messagebox
import pymysql




w3=Tk()
w3.geometry("490x270")
w3.title("email window")
w3.configure(bg='goldenrod')


def search():
    try:
        global ent1
        global ent2
        global ent3
        con = pymysql.connect(user='root', password='', \
                                  host='localhost', db='test')
        cur = con.cursor()
        sql = "select * from  phonebook where email='%s' " \
                 % (email.get())

        if email.get()=='' :
            messagebox.showinfo("ERROR","PLEASE ENTER EMAIL ID TO BE SEARCHED")
        elif not'@' in email.get():
            messagebox.showinfo("ERROR","PLEASE ENTER CORRECT EMAIL ID")

        else:
            cur.execute(sql)
            result = cur.fetchone()
            name.set(result[0])
            ent1 = Entry(w3, textvariable=name,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
            ent1.place(x=117,y=10)
            num.set(result[1])
            ent2 = Entry(w3,textvariable=num,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
            ent2.place(x=117,y=50)
            homen.set(result[3])
            ent3 = Entry(w3,textvariable=homen,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
            ent3.place(x=117,y=130)
            con.close()
    except:
        messagebox.showinfo('No Data', 'No such data available...')
    
       

def displayall():
    try:
        con = pymysql.connect(user='root', password='', \
                                  host='localhost', db='test')
        cur = con.cursor()
        sql = "select * from  phonebook where email='%s'"\
                %(email.get())
        cur.execute(sql)
        result=cur.fetchall()
        f=open('print.txt','w')
        for data in result:
            f.write("Name   :"+data[0]+"\nNumber :"+str(data[1])+"\nEmail  :"+data[2]+"\nTitle  :"+data[3])
        f.close()
        con.close()

        import subprocess as sp
        pName='notepad.exe'
        fName='print.txt'
        sp.Popen([pName,fName])
    except:
        messagebox.showinfo('No Data','No such data available...')

    
def Cleardisplay():
    email.set('')
    ent1.destroy()
    ent2.destroy()
    ent3.destroy()



l1 = Label(text='Name',font=('Calibri ',20),bg='goldenrod')
l1.place(x=10,y=10)
name = StringVar()

l2 = Label(text='Number',font=('Calibri ',20),bg='goldenrod')
l2.place(x=10,y=50)
num = StringVar()


l3 = Label(text='Email',font=('Calibri ',20),bg='goldenrod')
l3.place(x=10,y=90)
email=StringVar()
ent = Entry(w3,textvariable=email,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
ent.place(x=117,y=90)


l4 = Label(text='Title',font=('Calibri ',20),bg='goldenrod')
l4.place(x=10,y=130)
homen= StringVar()


search = Button(w3, height=1, width=17, bd=1, bg='cadet blue', font=('Calibri ', 15), text="search",command=search)
search.place(x=30, y=170)

clear = Button(w3, height=1, width=17, bd=1, bg='cadet blue', font=('Calibri ', 15), text="clear",command=Cleardisplay)
clear.place(x=240, y=170)

display=Button(w3, height=1, width=17, bd=1, bg='cadet blue', font=('Calibri ', 15), text="display",command=displayall)
display.place(x=130, y=230)


w3.mainloop()
