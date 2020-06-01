from tkinter import Tk,StringVar,ttk,messagebox
from tkinter import *
import time;
import datetime

root = Tk()
root.title("student attendance system")
root.geometry("1350x650+0+0")
root.configure(background="black")

LeftMayFrame= Frame(root,width=1000,height=650,bd=8,relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame= Frame(root,width=350,height=650,bd=8,relief="raise")
RightMayFrame.pack(side=RIGHT)


LeftMayFrame1= Frame(LeftMayFrame,width=1000,heigh=100,bd=8,relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2= Frame(LeftMayFrame,width=1000,heigh=550,bd=8,relief="raise")
LeftMayFrame2.pack(side=TOP)

RightMayFrame1= Frame(RightMayFrame,width=350,heigh=215,bd=8,relief="raise")
RightMayFrame1.pack(side=TOP)
RightMayFrame2= Frame(RightMayFrame,width=350,heigh=415,bd=8,relief="raise")
RightMayFrame2.pack(side=TOP)
#=================================================================================
cont1 = Canvas(RightMayFrame2, width=350, height=425,bg="white")
cont1.grid(row=0,column=0)
image5= PhotoImage(file="school.png")
cont1.create_image(200,200,image=image5)








                   


#=============================variables======================================

DateofOrder= StringVar()
value0= StringVar()
value1= StringVar()
value2= StringVar()
value3= StringVar()
value4= StringVar()
value5= StringVar()
value6= StringVar()
value7= StringVar()
value8= StringVar()
value9= StringVar()
value10= StringVar()
value11= StringVar()
value12= StringVar()

def MarkRegister():
    if value0.get() == "/" :
        value1.set("/")
        value2.set("/")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")
        value8.set("/")
        value9.set("/")
        value10.set("/")
        value11.set("/")
        value12.set("/")
    elif (value0.get() == "0"):
        value1.set("0")
        value2.set("0")
        value3.set("0")
        value4.set("0")
        value5.set("0")
        value6.set("0")
        value7.set("0")
        value8.set("0")
        value9.set("0")
        value10.set("0")
        value11.set("0")
        value12.set("0")
    elif (value0.get() == "S"):
        value1.set("S")
        value2.set("S")
        value3.set("S")
        value4.set("S")
        value5.set("S")
        value6.set("S")
        value7.set("S")
        value8.set("S")
        value9.set("S")
        value10.set("S")
        value11.set("S")
        value12.set("S")
    elif (value0.get() == "A"):
        value1.set("A")
        value2.set("A")
        value3.set("A")
        value4.set("A")
        value5.set("A")
        value6.set("A")
        value7.set("A")
        value8.set("A")
        value9.set("A")
        value10.set("A")
        value11.set("A")
        value12.set("A")
    elif (value0.get() == "L"):
        value1.set("L")
        value2.set("L")
        value3.set("L")
        value4.set("L")
        value5.set("L")
        value6.set("L")
        value7.set("L")
        value8.set("L")
        value9.set("L")
        value10.set("L")
        value11.set("L")
        value12.set("L")
    elif (value0.get() == " "):
        value1.set(" ")
        value2.set(" ")
        value3.set(" ")
        value4.set(" ")
        value5.set(" ")
        value6.set(" ")
        value7.set(" ")
        value8.set(" ")
        value9.set(" ")
        value10.set(" ")
        value11.set(" ")
        value12.set(" ")
            
        
def Reset ():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12.set("")
    
def qExit():
    qExit=messagebox.askyesno("Exit System","Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
    
#==============================components=======================================
DateofOrder.set(time.strftime("%d/%m/%Y"))
#==================================Leftframe1=====================================================
lblNo= Label(LeftMayFrame1,font=("arial",10,"bold"),text="No",bd=16)
lblNo.grid(row=0,column=0,sticky=W)
lblstudentNo=Label(LeftMayFrame1,font=("arial",10,"bold"),text="studentNo",bd=16)
lblstudentNo.grid(row=0,column=1,sticky=W)
lblstudentName=Label(LeftMayFrame1,font=("arial",10,"bold"),text="studentName",bd=16)
lblstudentName.grid(row=0,column=2,sticky=W)
lblcoursecode=Label(LeftMayFrame1,font=("arial",10,"bold"),text="course code",bd=16)
lblcoursecode.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame1,textvariable=value0,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=0,column=4)

btnFill= Button(LeftMayFrame1, text="Fill" , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1,command=MarkRegister).grid(row=0,column=5)

btnReset= Button(LeftMayFrame1, text="Reset" , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1,command=Reset).grid(row=0,column=6)

btnExit= Button(LeftMayFrame1, text="Exit" , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1,command=qExit).grid(row=0,column=7)

lblDateofOrder= Label(LeftMayFrame1,font=("arial",10,"bold"),textvariable=DateofOrder,padx=2,pady=2,bd=2,fg="black",bg="white",relief="sunken")
lblDateofOrder.grid(row=0,column=8,sticky=W)
#==================================Leftframe2 row=1=============================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="1",bd=16)
lblNo.grid(row=0,column=0,sticky=W)

lblstudentNo1=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1232",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo1.grid(row=0,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="SahithiElaprolu",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=0,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1005",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value1,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=0,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=0,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=0,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=0,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=0,column=8)
#==================================Leftframe2 row=2=================================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="2",bd=16)
lblNo.grid(row=1,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1235",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=1,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Sindhu Laskhmi",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=1,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1006",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=1,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value2,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=1,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=1,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=1,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=1,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=1,column=8)
#==================================Leftframe2 row=3=========================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="3",bd=16)
lblNo.grid(row=2,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1435",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=2,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Krishna",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=2,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1008",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=2,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value3,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=2,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=2,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=2,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=2,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=2,column=8)
#==================================Leftframe2 row=4=======================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="4",bd=16)
lblNo.grid(row=3,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1535",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=3,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Padma",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=3,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1017",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=3,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value4,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=3,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=3,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=3,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=3,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=3,column=8)
#==================================Leftframe2 row=5==========================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="5",bd=16)
lblNo.grid(row=4,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1605",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=4,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Harshitha",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=4,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1020",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=4,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value5,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=4,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=4,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=4,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=4,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=4,column=8)
#==================================Leftframe2 row=6===========================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="6",bd=16)
lblNo.grid(row=5,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1248",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=5,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="John Lucas",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=5,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1082",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=5,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value6,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=5,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=5,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=5,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=5,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=5,column=8)
#==================================Leftframe2 row=7===============================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="7",bd=16)
lblNo.grid(row=6,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1235",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=6,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Dong Lee",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=6,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1098",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=6,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value7,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=6,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=6,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=6,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=6,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=6,column=8)
#==================================Leftframe2 row=8==============================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="8",bd=16)
lblNo.grid(row=7,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1235",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=7,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Jungkook",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=7,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1074",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=7,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value8,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=7,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=7,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=7,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=7,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=7,column=8)
#==================================Leftframe2 row=9=============================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="9",bd=16)
lblNo.grid(row=8,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="2154",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=8,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Jimin",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=8,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1095",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=8,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value9,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=8,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=8,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=8,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=8,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=8,column=8)
#==================================Leftframe2 row=10============================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="10",bd=16)
lblNo.grid(row=9,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="2312",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=9,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Jin",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=9,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1071",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=9,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value10,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=9,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=9,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=9,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=9,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=9,column=8)
#==================================Leftframe2 row=11==============================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="11",bd=16)
lblNo.grid(row=10,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="2241",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=10,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Osaka Hiroshima",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=10,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1082",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value11,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=10,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=10,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=10,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=10,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=10,column=8)
#==================================Leftframe2 row=12============================================================================
lblNo= Label(LeftMayFrame2,font=("arial",10,"bold"),text="12",bd=16)
lblNo.grid(row=11,column=0,sticky=W)

lblstudentNo2=Label(LeftMayFrame2,font=("arial",10,"bold"),text="2541",padx=2,pady=2,bd=2,fg="black",width=18)
lblstudentNo2.grid(row=11,column=1,sticky=W)

lblstudentName=Label(LeftMayFrame2,font=("arial",10,"bold"),text="Nupita Yagasaki",padx=2,pady=2,bd=2,fg="black",width=12)
lblstudentName.grid(row=11,column=2,sticky=W)

lblcoursecode=Label(LeftMayFrame2,font=("arial",10,"bold"),text="1056",padx=2,pady=2,bd=2,fg="black",width=12)
lblcoursecode.grid(row=11,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value12,state="readonly")
box["values"]=('','/','L','0','A','S')
box.current(0)
box.grid(row=11,column=4)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=11,column=5)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=11,column=6)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=11,column=7)

btnSpace= Button(LeftMayFrame2, text=" " , padx=2, pady=2 , bd=2 , fg="black",font=("arial",10,"bold"),width=12,height=1).grid(row=11,column=8)








                    




























root.mainloop()
              
              
