from tkinter import *
from tkinter import messagebox

operator=''
def ClearDisplay():
    global operator
    operator=''
    name.set('')
    num.set('')

def namer():
    w1.destroy()
    from name import w5

def numberr():
    w1.destroy()
    from number import w2

def email():
    w1.destroy()
    from email import w3

w1 = Tk()
num = StringVar()
name = StringVar()
w1.geometry("550x310")
w1.title("search window")
w1.configure(bg='goldenrod')

l1 = Label(w1,text='BY WHAT FIELD DO YOU WANT TO SEARCH??',font=('Calibri ',18),bg='goldenrod')
l1.place(x=10,y=10)

search = Button(w1, height=1, width=17, bd=1, bg='gold', font=('Calibri ', 15), text="search by name",command=namer)
search.place(x=180, y=80)

search1=Button(w1,height=1,width=17,bd=1,bg='gold',font=('Calibri ', 15),text="search by number",command=numberr)
search1.place(x=180,y=140)

search2=Button(w1,height=1,width=17,bd=1,bg='gold',font=('Calibri ', 15),text="search by email",command=email)
search2.place(x=180,y=200)

w1.mainloop()
