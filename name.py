from tkinter import *
from tkinter import messagebox
import pymysql

w5=Tk()
w5.geometry("490x270")
w5.title("name window")
w5.configure(bg='goldenrod')

def search():
    try:
        global ent1
        global ent2
        global ent3
        con = pymysql.connect(user='root', password='', \
                                  host='localhost', db='test')
        cur = con.cursor()
        sql = "select * from  phonebook where name='%s' " \
                 % (name.get())
        if name.get()=='':
            messagebox.showinfo("ERROR","PLEASE ENTER NAME TO BE SEARCHED")
        else:
            cur.execute(sql)
            result = cur.fetchone()
            num.set(result[1])
            ent1 = Entry(w5,textvariable=num,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
            ent1.place(x=117,y=50)
            email.set(result[2])
            ent2 = Entry(w5,textvariable=email,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
            ent2.place(x=117,y=90)
            homen.set(result[3])
            ent3 = Entry(w5,textvariable=homen,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
            ent3.place(x=117,y=130)
            con.close()
    except:
        messagebox.showinfo('No Data', 'No such data available...')
            
def Cleardisplay():
    name.set('')
    ent1.destroy()
    ent2.destroy()
    ent3.destroy()

def displayall():
    try:
        con = pymysql.connect(user='root', password='', \
                                  host='localhost', db='test')
        cur = con.cursor()
        sql = "select * from  phonebook where name='%s'"\
                %(name.get())
        cur.execute(sql)
        result=cur.fetchall()
        f=open('print.txt','w')
        for data in result:
            f.write(str(data)+'\n')
        f.close()
        con.close()

        import subprocess as sp
        pName='notepad.exe'
        fName='print.txt'
        sp.Popen([pName,fName])
    except:
        messagebox.showinfo('No Data','No such data available...')

l1 = Label(text='Name',font=('Calibri ',20),bg='goldenrod')
l1.place(x=10,y=10)
name = StringVar()
ent = Entry(w5, textvariable=name,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
ent.place(x=117,y=10)
ent.focus()

l2 = Label(text='Number',font=('Calibri ',20),bg='goldenrod')
l2.place(x=10,y=50)
num = StringVar()

l3 = Label(text='Email',font=('Calibri ',20),bg='goldenrod')
l3.place(x=10,y=90)
email=StringVar()

l4 = Label(text='Title',font=('Calibri ',20),bg='goldenrod')
l4.place(x=10,y=130)
homen= StringVar()

search = Button(w5, height=1, width=17, bd=1, bg='cadet blue', font=('Calibri ', 15), text="search",command=search)
search.place(x=30, y=170)

clear = Button(w5, height=1, width=17, bd=1, bg='cadet blue', font=('Calibri ', 15), text="clear",command=Cleardisplay)
clear.place(x=240, y=170)

display=Button(w5, height=1, width=17, bd=1, bg='cadet blue', font=('Calibri ', 15), text="display",command=displayall)
display.place(x=130, y=230)

w5.mainloop()
