import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Registration:
    def __init__(self,root):
        self.root=root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

        Date_Of_Registration=StringVar()
        Date_Of_Registration.set(time.strftime("%d/%m/%y"))

        Ref=StringVar()
        Mobile_No=StringVar()
        Pincode=StringVar()
        Address=StringVar()
        Firstname=StringVar()
        Lastname=StringVar()

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=IntVar()

        Membership=StringVar()
        Membership.set("0")

        def exitbtt():
            exitbtt=tkinter.messagebox.askyesno("Member registration From","Are you sure you want to exit?")
            if(exitbtt>0):
               root.destroy()
               return
        def reesetbtn():
            reesetbtn=tkinter.messagebox.askokcancel("Member Registration Form","You want to add as new record")
            if(reesetbtn>0):
                resetbtn()
            elif reesetbtn<=0:
                resetbtn()
                detail_labeltxt.delete("1.0",END)
                return
        def Reference_num():
            rannumber=random.randint(10000,999999)
            randomnumber=str(rannumber)
            Ref.set(randomnumber)
        
        def membership_fees():
            if(var5.get()==1):
                member_membershiptxt.configure(state=NORMAL)
                item=float(15000)
                Membership.set(str(item)+"Rs")
            elif(var5.get()==0):
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")
        def Receipt():
            Reference_num()
            detail_labeltxt.insert(END,"\t"+Date_Of_Registration.get()+"\t\t"+Ref.get()+"\t"+
                                   Firstname.get()+"\t"+Lastname.get()+"\t\t"+Mobile_No.get()+"\t"+Address.get()+"\t\t"+Pincode.get()+
                                   "\t"+member_gendercmb.get()+"\t"+Membership.get()+"\n")
            

        title=Label(self.root,text="Member Registration Form",font=("monotype corsiva",30,"bold"),bd=5,relief=GROOVE,bg="#E6005C",fg="#000000")
        title.pack(side=TOP,fill=X)

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#001a66")
        Manage_Frame.place(x=20,y=100,width=450,height=630)

        Cus_title=Label(Manage_Frame,text="Customer Details",font=("arial",20,"bold"),bg="#001a66",fg="white")
        Cus_title.grid(row=0,columnspan=2,pady=5)

        member_date1b1=Label(Manage_Frame,text="Date",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_date1b1.grid(row=1,column=0,pady=5,padx=10,sticky="w")

        member_datetxt=Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Date_Of_Registration)
        member_datetxt.grid(row=1,column=1,padx=10,pady=5,sticky="w")

        member_ref1b1=Label(Manage_Frame,text="Reference ID",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_ref1b1.grid(row=2,column=0,padx=10,pady=5,sticky="w")

        member_reftxt=Entry(Manage_Frame,font=("arial",15,"bold"),state=DISABLED,text=Ref)
        member_reftxt.grid(row=2,column=1,padx=10,pady=5,sticky="w")

        member_fname1b1=Label(Manage_Frame,text="First Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_fname1b1.grid(row=3,column=0,pady=5,padx=10,sticky="w")
        
        member_nametxt=Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Firstname)
        member_nametxt.grid(row=3,column=1,padx=10,pady=5,sticky="w")

        member_lname1b1=Label(Manage_Frame,text="Last Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_lname1b1.grid(row=4,column=0,pady=5,padx=10,sticky="w")

        member_lametxt=Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Lastname)
        member_lametxt.grid(row=4,column=1,padx=10,pady=5,sticky="w")

        member_mobile1b1=Label(Manage_Frame,text="Mobile No",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_mobile1b1.grid(row=5,column=0,pady=5,padx=10,sticky="w")

        member_mobiletxt=Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Mobile_No)
        member_mobiletxt.grid(row=5,column=1,padx=10,pady=5,sticky="w")

        member_address1b1=Label(Manage_Frame,text="Address",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_address1b1.grid(row=6,column=0,pady=5,padx=10,sticky="w")

        member_addresstxt=Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Address)
        member_addresstxt.grid(row=6,column=1,padx=10,pady=5,sticky="w")

        member_pincode1b1=Label(Manage_Frame,text="Pin code",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_pincode1b1.grid(row=7,column=0,pady=5,padx=10,sticky="w")

        member_pincodetxt=Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Pincode)
        member_pincodetxt.grid(row=7,column=1,padx=10,pady=5,sticky="w")

        member_gender1b1=Label(Manage_Frame,text="Gender",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_gender1b1.grid(row=8,column=0,pady=5,padx=10,sticky="w")

        member_gendercmb=ttk.Combobox(Manage_Frame,text=var4,state="readonly",font=("arial",15,"bold"),width=19)
        member_gendercmb['values']=("","Male","Female","Others")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8,column=1,padx=10,pady=5,sticky="w")

        member_id_prroflb1=Label(Manage_Frame,text="ID Proof",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_id_prroflb1.grid(row=9,column=0,pady=5,padx=10,sticky="w")

        member_id_prrofcmb=ttk.Combobox(Manage_Frame,text=var3,state="readonly",font=("arial",15,"bold"),width=19)
        member_id_prrofcmb['values']=("","Aadhar Card","Passport","Driving License","Pan Card","Student ID")
        member_id_prrofcmb.current(0)
        member_id_prrofcmb.grid(row=9,column=1,padx=10,pady=5,sticky="w")

        member_memtypelb1=Label(Manage_Frame,text="Member Type",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_memtypelb1.grid(row=10,column=0,pady=5,padx=10,sticky="w")

        member_memtypecmb=ttk.Combobox(Manage_Frame,text=var2,state="readonly",font=("arial",15,"bold"),width=19)
        member_memtypecmb['values']=("","Ayushman Card","Insurance","Pay Imedialtely","Pay when leaving")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10,column=1,padx=10,pady=5,sticky="w")

        member_paymentwithlb1=Label(Manage_Frame,text="Payment",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_paymentwithlb1.grid(row=11,column=0,pady=5,padx=10,sticky="w")

        member_paymentwithcmb=ttk.Combobox(Manage_Frame,text=var1,state="readonly",font=("arial",15,"bold"),width=19)
        member_paymentwithcmb['values']=("","Cash","Debit Card-Rupay","Debit Card-Visa","Debit Card-Mastercard","Credit Card","Phonepay","GPay","Paytm")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row=11,column=1,padx=10,pady=5,sticky="w")

        member_membership=Checkbutton(Manage_Frame,text="Membership fess",variable=var5,onvalue=1,offvalue=0,font=("arial",15,"bold"),bg="#001a66",fg="white",command=membership_fees)
        member_membership.grid(row=12,column=0,sticky="w")
        member_membershiptxt=Entry(Manage_Frame,font=("arial",15,"bold"),state=DISABLED,justify=RIGHT,textvariable=Membership)
        member_membershiptxt.grid(row=12,column=1,padx=10,pady=5,sticky="w")

        detail_frame=Frame(self.root,relief=RIDGE,bg="#001a66")
        detail_frame.place(x=500,y=100,width=820,height=630)

        detail_label=Label(detail_frame,font=("arial",11,"bold"),padx=0,pady=0,width=95,text="Date\t Ref ID\tFirstname    Lastname   Mobile Mo      Address     Pincode    Gender     Membership")
        detail_label.grid(row=0,column=0,columnspan=4,sticky="w")
        detail_labeltxt=Text(detail_frame,width=123,height=34,font=("arial",10))
        detail_labeltxt.grid(row=1,column=0,columnspan=4)

        receiptbtn=Button(detail_frame,padx=15,pady=15,bd=5,font=("arial",12,"bold"),bg="#ff9966",width=20,text="Receipt",command=Receipt)
        receiptbtn.grid(row=2,column=0)

        resetbtn=Button(detail_frame,padx=15,pady=15,bd=5,font=("arial",12,"bold"),bg="#ff9966",width=20,text="Reset",command=reesetbtn)
        resetbtn.grid(row=2,column=1)

        exitbtn=Button(detail_frame,padx=15,pady=15,bd=5,font=("arial",12,"bold"),bg="#ff9966",width=20,text="Exit",command=exitbtt)
        exitbtn.grid(row=2,column=2)

if __name__=="__main__":
    root=Tk()
    app=Registration(root)
    root.mainloop()