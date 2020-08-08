import pymysql
from tkinter import *
from tkinter import messagebox

phonebook = Tk()
phonebook.title('Phone Directory')
phonebook.configure(bg='goldenrod')
phonebook.geometry("1200x680")
phonebook.resizable(0,0)

i=50
def set_y():
    global i
    i=i+25

c=0
def click():
    global c
    c=c+1
    
def datatable():
    data = Label(text='PHONE RECORD',font=('Calibri ',20),bg='goldenrod')
    data.place(x=720,y=10)
    data = Label(text='NAME\t',font=('Calibri ',10),padx=30,bg='gold')
    data.place(x=500,y=50)
    data = Label(text='NUMBER',font=('Calibri ',10),padx=30,bg='gold')
    data.place(x=610,y=50)
    data = Label(text='EMAIL',font=('Calibri ',10),padx=100,bg='gold')
    data.place(x=738,y=50)
    data = Label(text='TITLE',font=('Calibri ',10),padx=30,bg='gold')
    data.place(x=990,y=50)
datatable()
        
def table(result):
    global data,size
    size=len(result)
    #if c>1:
    i=50
    #else:
    #    set_y()
    for m in range (0,len(result)):
        n=0
        #if c>1:
        i+=25
        #if c==0:
        #    set_y()
        data = Label(text=result[m][n],font=('Calibri ',10),bg='goldenrod')
        data.place(x=500,y=i)
        data = Label(text=result[m][n+1],font=('Calibri ',10),bg='goldenrod')
        data.place(x=610,y=i)
        data= Label(text=result[m][n+2],font=('Calibri ',10),bg='goldenrod')
        data.place(x=738,y=i)
        data = Label(text=result[m][n+3],font=('Calibri ',10),bg='goldenrod')
        data.place(x=990,y=i)

def refresh(size):
    i=50
    for m in range (0,size*c):
        n=0
        i=i+25
        data = Label(text="\t\t\t\t",font=('Calibri ',10),bg='goldenrod')
        data.place(x=500,y=i)
        data = Label(text="\t\t\t\t",font=('Calibri ',10),bg='goldenrod')
        data.place(x=610,y=i)
        data= Label(text="\t\t\t\t",font=('Calibri ',10),bg='goldenrod')
        data.place(x=738,y=i)
        data = Label(text="\t\t\t\t",font=('Calibri ',10),bg='goldenrod')
        data.place(x=990,y=i)
        
l1 = Label(text='Name',font=('Calibri ',20),bg='goldenrod')
l1.place(x=10,y=10)
name = StringVar()
ent = Entry(phonebook, textvariable=name,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
ent.place(x=117,y=10)
ent.focus()

l2 = Label(text='Number',font=('Calibri ',20),bg='goldenrod')
l2.place(x=10,y=50)
num = StringVar()
ent = Entry(phonebook,textvariable=num,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
ent.place(x=117,y=50)

l3 = Label(text='Email',font=('Calibri ',20),bg='goldenrod')
l3.place(x=10,y=90)
email=StringVar()
ent = Entry(phonebook,textvariable=email,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
ent.place(x=117,y=90)

l4 = Label(text='Title',font=('Calibri ',20),bg='goldenrod')
l4.place(x=10,y=130)
title= StringVar()
ent = Entry(phonebook,textvariable=title,font=('Calibri ',20),bd=1,bg='lightgoldenrod',insertwidth=5)
ent.place(x=117,y=130)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    num.set(operator)

operator = ' '
def ClearDisplay():
    global operator
    operator=''
    name.set('')
    num.set('') 
    title.set('')
    email.set('')

def displayall():
    click()
    try:
        con = pymysql.connect(user='root', password='', \
                                  host='localhost', db='test')
        cur = con.cursor()
        sql = "select * from  phonebook"
        cur.execute(sql)
        result=cur.fetchall()
        #print("|NAME\t\t\t|Number\t\t\t|EMAIL\t\t\t|TITLE\t")
        f=open('print.rtf','w')
        #for m in range (0,4):
         #   n=0
          #  print("|",result[m][n]," \t\t|",result[m][n+1],"\t\t|",result[m][n+2],"\t|",result[m][n+3])
        #for data in result:
        for m in range (0,len(result)):
            n=0
            f.write("|"+str(result[m][n])+"  \t\t|"+str(result[m][n+1])+"\t\t|"+str(result[m][n+2])+"\t\t|"+str(result[m][n+3])+"\n")
            #f.write(str(data)+'\n')
        f.close()
        con.close()
        #import subprocess as sp
        #import os
        #os.startfile('print.rtf')
        #pName='notepad.exe'
        #fName='print.rtf'
        #sp.Popen([pName,fName])
    except:
        messagebox.showinfo('No Data','No such data available...')
    table(result)
displayall()

list1=[]
list2=[]
list3=[]
list4=[]
def save_contact():
    click()
    global k,v,g,t
    try:
        con=pymysql.connect(user='root',password='',\
                            host='localhost',db='test')
        cur=con.cursor()
        k=name.get()
        v=num.get()
        g=email.get()
        t=title.get()

        if k in list1 :
            messagebox.showinfo("REPEAT ERROR !","name already in database")
        elif v in list2:
            messagebox.showinfo("REPEAT ERROR !","number already in database")
        elif g in list3:
            messagebox.showinfo("REPEAT ERROR !","email already in database")
        #elif t in list4:
        #messagebox.showinfo("REPEAT","title already in database")
        elif not '@' in g:
            messagebox.showinfo('ERROR',"enter correct email id")
        #elif name.get()==''or num.get()=='' or email.get()=='' :
            #messagebox.showinfo("please enter this fields")
        else:
            sql="insert into phonebook values('%s' ,'%s','%s','%s')"\
                %(name.get(),num.get(),email.get(),title.get())
            cur.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo("Success !","Record saved ")
            list1.append(k)
            list2.append(v)
            list3.append(g)
            list4.append(t)
            #print(list1,list2,list3,list4)
    except:
        messagebox.showinfo("Oops!","Error in data entry...")
    finally:
        ClearDisplay()
    refresh(size)
    #displayall()
            
def update_contact():
    click()
    #from update import up
    try:
        con = pymysql.connect(user='root', password='', host='localhost', db='test')
        cur = con.cursor()
        sql = "update phonebook set number='%s',email='%s',title='%s' where name='%s' " \
              % (num.get(),email.get(),title.get(),name.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("Success"," Record updated ")
    except:
        messagebox.showinfo("Oops!","Error occured ")
    finally:
        ClearDisplay()
    refresh(size)
    #displayall()
    
def search_contact():
    phonebook.destroy()
    from search import  w1

def remove_contact():
    click()
    try:
        if(num.get()==''):
            con = pymysql.connect(user='root', password='', \
                                  host='localhost', db='test')
            cur = con.cursor()
            sql = "delete from  phonebook where name='%s' " \
                  % (name.get())
            cur.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo("Success,Record deleted...")
        else:
            con = pymysql.connect(user='root', password='', \
                                  host='localhost', db='test')
            cur = con.cursor()
            sql = "delete from  phonebook where number='%s' " \
                  % (num.get())
            cur.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo("Success,Record deleted...")
    except:
        messagebox.showinfo("Error", "Error occured...")
    finally:
        ClearDisplay()
    refresh(size)
    #displayall()

"""def displayall():
    click()
    try:
        con = pymysql.connect(user='root', password='', \
                                  host='localhost', db='test')
        cur = con.cursor()
        sql = "select * from  phonebook"
        cur.execute(sql)
        result=cur.fetchall()
        print("|NAME\t\t\t|Number\t\t\t|EMAIL\t\t\t|TITLE\t")
        f=open('print.rtf','w')
        for m in range (0,4):
            n=0
            print("|",result[m][n]," \t\t|",result[m][n+1],"\t\t|",result[m][n+2],"\t|",result[m][n+3])
        #for data in result:
        for m in range (0,len(result)):
            n=0
            f.write("|"+str(result[m][n])+"\t\t|"+str(result[m][n+1])+"\t\t|"+str(result[m][n+2])+"\t|"+str(result[m][n+3])+"\n")
            #f.write(str(data)+'\n')
        f.close()
        con.close()
        #import subprocess as sp
        #pName='notepad.exe'
        #fName='print.rtf'
        #sp.Popen([pName,fName])
    except:
        messagebox.showinfo('No Data','No such data available...')
    table(result)"""

def print_it():
    import os
    os.startfile('print.rtf')
    
def create_button():
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn0,btnclear
    btn1=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="1",command=lambda: btnClick(1))
    btn1.place(x=15,y=190)
    btn2=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="2",command=lambda: btnClick(2))
    btn2.place(x=170,y=190)
    btn3=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="3",command=lambda: btnClick(3))
    btn3.place(x=325,y=190)
    btn4=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="4",command=lambda: btnClick(4))
    btn4.place(x=15,y=260)
    btn5=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="5",command=lambda: btnClick(5))
    btn5.place(x=170,y=260)
    btn6=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="6",command=lambda: btnClick(6))
    btn6.place(x=325,y=260)
    btn7=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="7",command=lambda: btnClick(7))
    btn7.place(x=15,y=330)
    btn8=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="8",command=lambda: btnClick(8))
    btn8.place(x=170,y=330)
    btn9=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="9",command=lambda: btnClick(9))
    btn9.place(x=325,y=330)
    btn0=Button(phonebook,height=2,width=7,bd=1,bg='goldenrod',font=('Calibri ', 15),text="0",command=lambda: btnClick(0))
    btn0.place(x=170,y=400)
    btnclear=Button(phonebook,height=2,width=7,bd=1,bg='red',font=('Calibri ', 15),text="clear",command=ClearDisplay)
    btnclear.place(x=15,y=400)
    save=Button(phonebook,height=2,width=7,bd=1,bg='LawnGreen',font=('Calibri ', 15),text="SAVE",command=save_contact)
    save.place(x=15,y=470)
    update=Button(phonebook,height=2,width=7,bd=1,bg='Orange',font=('Calibri ', 15),text="UPDATE",command=update_contact)
    update.place(x=170,y=470)
    search=Button(phonebook,height=2,width=7,bd=1,bg='cadet blue',font=('Calibri ', 15),text="SEARCH",command=search_contact)
    search.place(x=325,y=400)
    remove=Button(phonebook,height=2,width=7,bd=1,bg='coral',font=('Calibri ', 15),text="REMOVE",command=remove_contact)
    remove.place(x=325,y=470)
    display=Button(phonebook, height=2, width=35, bd=1, bg='YELLOW', font=('Calibri ', 15), text="DISPLAY",command=displayall)
    display.place(x=15,y=540)
    p=Button(phonebook, height=2, width=35, bd=1, bg='BROWN', font=('Calibri ', 15), text="PRINT COPY",command=print_it)
    p.place(x=15,y=610)
create_button()


phonebook.mainloop()
