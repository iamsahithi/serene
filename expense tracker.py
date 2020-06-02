from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry

def Addexpense():
    a= Edate.get()
    b=Title.get()
    c=Expense.get()
    data=[a,b,c]
    print(data)
    TVExpense.insert("","end",values=data)
root = Tk()
root.title("Expense Tracker")
root.geometry("700x500")
#root.state("zoomed")
Tab=Notebook(root)


F1= Frame(Tab,width=500,height=500)
F2=Frame(Tab,width=500,height=500)
Tab.add(F1,text="Expense")
Tab.add(F2,text="Income")
Tab.pack(fill=BOTH,expand=1)

#=======TAB1 EXPENSE================
Date=ttk.Label(F1,text="Date",font=(None,18))
Date.grid(row=0,column=0,padx=5,pady=5,sticky="w")

Edate =DateEntry(F1,width=19,background="blue",foregroud="white",font=(None,18))
Edate.grid(row=0,column=1,padx=5,pady=5,sticky="w")


LTitle=ttk.Label(F1,text="Title",font=(None,18))
LTitle.grid(row=1,column=0,padx=5,pady=5,sticky="w")

Title=StringVar()

Etitle=ttk.Entry(F1,textvariable=Title,font=(None,18))
Etitle.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#=============================================

LExpense=ttk.Label(F1,text="Expense",font=(None,18))
LExpense.grid(row=2,column=0,padx=5,pady=5,sticky="w")

Expense= StringVar()

EExpense=ttk.Entry(F1,textvariable=Expense,font=(None,18))
EExpense.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#=================================================
Badd =Button(F1,text="ADD",command=Addexpense)
Badd.grid(row=3,column=1,padx=5,pady=5,sticky="w",ipadx=10,ipady=10)

TVList = ["Date","Expense","Income"]
TVExpense=ttk.Treeview(F1,column=TVList,show="headings",height=5)
for i in TVList:
    TVExpense.heading(i,text=i.title())
TVExpense.grid(row=4,column=0,padx=5,pady=5,sticky="w",columnspan=3)








root.mainloop()
