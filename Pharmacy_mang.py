import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
def main():
    root=Tk()
    app=windows1(root)
    root.mainloop()
    

class windows1:
    def __init__(self,master):
        self.master=master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+-0+0')
        self.frame=Frame(self.master)
        self.frame.pack()
        self.master.configure(background="black")
        self.frame.configure(background="black")

        self.UserName=StringVar()
        self.Password=StringVar()

        self.LableTitle=Label(self.frame,text="        Pharmacy Management System        ",font=("arial","40","bold"),bd=5,relief="sunken",)
        self.LableTitle.grid(row=0,column=0,columnspan=2,pady=20)
        self.Loginframe1=Frame(self.frame,width=1000,height=300,bd=10,relief="groove")
        self.Loginframe1.grid(row=1,column=0)

        self.LableUserName=Label(self.Loginframe1,text="User Name",font=("arial",20,"bold"),bd=3)
        self.LableUserName.grid(row=0,column=0)
        self.textUserName=Entry(self.Loginframe1,font=("arial",20,"bold"),bd=3,textvariable=self.UserName)
        self.textUserName.grid(row=0,column=1,padx=50,pady=50)

        self.LablePassword=Label(self.Loginframe1,text="Password",font=("arial",20,"bold"),bd=3)
        self.LablePassword.grid(row=1,column=0)
        self.textPassword=Entry(self.Loginframe1,font=("arial",20,"bold"),show="*",bd=3,textvariable=self.Password)
        self.textPassword.grid(row=1,column=1,padx=40,pady=15)

        self.Loginframe2=Frame(self.frame,width=1000,height=100,bd=10,relief="groove")
        self.Loginframe2.grid(row=2,column=0,pady=15)
        self.button_login=Button(self.Loginframe2,text="Login",width=20,font=("arial",18,"bold"),command=self.login_system)
        self.button_login.grid(row=0,column=0,padx=10,pady=10)
        self.button_reset=Button(self.Loginframe2,text="Reset",width=20,font=("arial",18,"bold"),command=self.reset_btn)
        self.button_reset.grid(row=0,column=3,padx=10,pady=10)
        self.button_exit=Button(self.Loginframe2,text="Exit",width=20,font=("arial",18,"bold"),command=self.Exit_btn)
        self.button_exit.grid(row=0,column=6,padx=10,pady=10)

        self.Loginframe3=Frame(self.frame,width=1000,height=200,bd=10,relief="groove")
        self.Loginframe3.grid(row=6,column=0,pady=5)

        self.button_reg=Button(self.Loginframe3,text="Patient Registration Window",state=DISABLED,font=("arial",15,"bold"),command=self.Registration_window)
        self.button_reg.grid(row=0,column=0,padx=10,pady=10)
        self.button_Hosp=Button(self.Loginframe3,text="Hospital Management Window",state=DISABLED,font=("arial",15,"bold"),command=self.Hospital_window)
        self.button_Hosp.grid(row=0,column=1,padx=10,pady=10)
        self.button_Dr_appt=Button(self.Loginframe3,text="Doctor Management Window",state=DISABLED,font=("arial",15,"bold"),command=self.Dotor_Appointment_window)
        self.button_Dr_appt.grid(row=1,column=0,padx=10,pady=10)

    def login_system(self):
        user=self.UserName.get()
        pswd=self.Password.get()
        if(user==str("admin") and (pswd==str("admin"))):
            tkinter.messagebox.askyesno("Pharmacy Management System","Login Succussfull")
            self.button_reg.config(state=NORMAL)
            self.button_Hosp.config(state=NORMAL)
            self.button_Dr_appt.config(state=NORMAL)
            self.button_med_stock.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System","You have ented an invalid username or password")
            self.button_reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_appt.config(state=DISABLED)
            self.button_med_stock.config(state=DISABLED)

            self.UserName.set("")
            self.Password.set("")
            self.textUserName.focus()
    def reset_btn(self):
        self.button_reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_appt.config(state=DISABLED)
        self.button_med_stock.config(state=DISABLED)
        self.UserName.set("")
        self.Password.set("")
        self.textUserName.focus()
    def Exit_btn(self):
        self.Exit_btn=tkinter.messagebox.askyesno("Pharmacy Management System","Are you sure you want to exit?")
        if(self.Exit_btn>0):
            self.master.destroy()
            return

    def Registration_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Registration(self.newWindow)
    def Hospital_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Hospital(self.newWindow)
    def Dotor_Appointment_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Doctor(self.newWindow)


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

class Hospital():
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref=StringVar()
        cmbTabletNames=StringVar()
        HospitalCode=StringVar()
        Number_of_Tablets=StringVar()
        Lot=StringVar()
        IssueDate=StringVar()
        ExpiryDate=StringVar()
        DailyDose=StringVar()
        SideEffects=StringVar()
        MoreInformation=StringVar()
        StorageAdvise=StringVar()
        Medication=StringVar()
        PatientId=StringVar()
        PatientNHnumber=StringVar()
        PatientName=StringVar()
        Dateofbirth=StringVar()
        PatientAdress=StringVar()
        Prescription=StringVar()
        NHSnumber=StringVar()

        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        def Reference_numfunc():
            ranumber=random.randint(10000,999999)
            randomnumber=str(ranumber)
            Ref.set(randomnumber)

        def prescriptiondata():
            Reference_numfunc()
            TextPrescription.insert(END,"Patient ID:\t\t"+PatientId.get()+"\n")
            TextPrescription.insert(END,"Patient Name:\t\t"+PatientName.get()+"\n")
            TextPrescription.insert(END,"Tablet:\t\t"+cmbTabletNames.get()+"\n")
            TextPrescription.insert(END,"Number of tablet:\t\t"+Number_of_Tablets.get()+"\n")
            TextPrescription.insert(END,"Daily Dose:\t\t"+DailyDose.get()+"\n")
            TextPrescription.insert(END,"Issued Date:\t\t"+IssueDate.get()+"\n")
            TextPrescription.insert(END,"Expiry Date:\t\t"+ExpiryDate.get()+"\n")
            TextPrescription.insert(END,"Storage:\t\t"+StorageAdvise.get()+"\n")
            TextPrescription.insert(END,"More Information:\t\t"+MoreInformation.get()+"\n")
            return

        def prescriptiondatafunc():
            Reference_numfunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+Ref.get()+"\t"+
                                        "\t"+PatientName.get()+"\t\t"+Dateofbirth.get()+"\t\t"+NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t\t"+
                                        Number_of_Tablets.get()+"\t\t"+IssueDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t"+
                                        StorageAdvise.get()+"\t"+PatientId.get()+"\n")
            return

        def exitbtn():
            exitbtn=tkinter.messagebox.askyesno("Hospital Management System","Are you sure you want to exit?")
            if(exitbtn>0):
               root.destroy()
               return
        def deletefunc():
            Ref=set("")
            cmbTabletNames=set("")
            HospitalCode=set("")
            Number_of_Tablets=set("")
            Lot=set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvise.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            PatientName.set("")
            Dateofbirth.set("")
            PatientAdress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return
        def reesetfunc():
            Ref=set("")
            cmbTabletNames=set("")
            HospitalCode=set("")
            Number_of_Tablets=set("")
            Lot=set("")
            IssueDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvise.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumber.set("")
            PatientName.set("")
            Dateofbirth.set("")
            PatientAdress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPrescriptionData("1.0",END)
            return
            
        title=Label(self.root,text="Hospital Management System",font=("monotype corsiva",42,"bold"),bd=5,relief=GROOVE,bg="#2eb8b8",fg="black")
        title.pack(side=TOP,fill=X)

        Manage_Frame=Frame(self.root,width=1510,height=400,bd=5,relief=RIDGE,bg="#0099cc")
        Manage_Frame.place(x=10,y=80)

        Button_Frame=Frame(self.root,width=1510,height=55,bd=4,relief=RIDGE,bg="#328695")
        Button_Frame.place(x=10,y=460)

        Data_Frame=Frame(self.root,width=1510,height=270,bd=4,relief=RIDGE,bg="#266e73")
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft=LabelFrame(Manage_Frame,width=1050,text="General Information",font=("arial",20,"italic bold"),height=390,bd=7,relief=RIDGE,bg="#0099cc")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight=LabelFrame(Manage_Frame,width=1050,text="Prescription",font=("arial",15,"italic bold"),height=390,bd=7,relief=RIDGE,bg="#0099cc")
        Data_FrameRight.pack(side=RIGHT)

        Data_Framedata=LabelFrame(Data_Frame,width=1050,text="Prescription Data",font=("arial",15,"italic bold"),height=390,bd=4,relief=RIDGE,bg="#3eb7bb")
        Data_Framedata.pack(side=LEFT)

        Datelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date",padx=2,bg="#0099cc")
        Datelb1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        Datetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Date_of_Registration)
        Datetxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)

        Reflb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Reference Number",padx=2,bg="#0099cc")
        Reflb1.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        Reftxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,state=DISABLED,textvariable=Ref)
        Reftxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)

        PatientIdlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Id",padx=2,bg="#0099cc")
        PatientIdlb1.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        PatientIdtxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PatientId)
        PatientIdtxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)

        PatientNamelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Name",padx=2,bg="#0099cc")
        PatientNamelb1.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        PatientNametxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PatientName)
        PatientNametxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)

        Dateofbirthlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date of Birth",padx=2,bg="#0099cc")
        Dateofbirthlb1.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        Dateofbirthtxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Dateofbirth)
        Dateofbirthtxt.grid(row=4,column=1,padx=10,pady=5,sticky=E)

        Addresslb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Address",padx=2,bg="#0099cc")
        Addresslb1.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        Addresstxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PatientAdress)
        Addresstxt.grid(row=5,column=1,padx=10,pady=5,sticky=E)

        NHSnumberlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="NHS Unique Number",padx=2,bg="#0099cc")
        NHSnumberlb1.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        NHSnumbertxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)

        Tabletlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Tablet",padx=2,bg="#0099cc")
        Tabletlb1.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        Tabletcmb=ttk.Combobox(Data_FrameLeft,textvariable=cmbTabletNames,width=25,state="readonly,"
                               ,font=("arial",12,"bold"))
        Tabletcmb['values']=("","Paracetamol","Dan-p","Dio-1 One","Calpol","Amlodipine Besylate","Nexium","Singulair","Plavis","Amoxicillian","Azithromycin","Limcin-900")
        Tabletcmb.current(0)
        Tabletcmb.grid(row=7,column=1,padx=10,pady=5)

        No_of_Tabletslb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Number of Tablets",padx=2,bg="#0099cc")
        No_of_Tabletslb1.grid(row=8,column=0,padx=10,pady=5,sticky=W)
        No_of_Tabletstxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Number_of_Tablets)
        No_of_Tabletstxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)

        HospitalCodelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Hospital Code",padx=2,bg="#0099cc")
        HospitalCodelb1.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        HospitalCodetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable=HospitalCode)
        HospitalCodetxt.grid(row=0,column=3,padx=10,pady=5,sticky=E)

        StorageAdviselb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Storage Advise",padx=2,bg="#0099cc")
        StorageAdviselb1.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        StorageAdvisecmb=ttk.Combobox(Data_FrameLeft,textvariable=StorageAdvise,width=23,state="readonly,"
                               ,font=("arial",12,"bold"))
        StorageAdvisecmb['values']=("","Under room temp","below 5*C","below 0*C","Refrigration")
        StorageAdvisecmb.current(0)
        StorageAdvisecmb.grid(row=1,column=3,padx=10,pady=5,sticky=E)

        Lot_nolb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Lot Number",padx=2,bg="#0099cc")
        Lot_nolb1.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Lot_notxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable=Lot)
        Lot_notxt.grid(row=2,column=3,padx=10,pady=5,sticky=E)

        IssueDatelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date of Issue",padx=2,bg="#0099cc")
        IssueDatelb1.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        IssueDatetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable=IssueDate)
        IssueDatetxt.grid(row=3,column=3,padx=10,pady=5,sticky=E)

        ExpiryDatelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date of Expiry",padx=2,bg="#0099cc")
        ExpiryDatelb1.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        ExpiryDatetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4,column=3,padx=10,pady=5,sticky=E)

        DailyDoselb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Daily Dossage",padx=2,bg="#0099cc")
        DailyDoselb1.grid(row=5,column=2,padx=10,pady=5,sticky=W)
        DailyDosetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable=DailyDose)
        DailyDosetxt.grid(row=5,column=3,padx=10,pady=5,sticky=E)

        SideEffectslb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Side Effects",padx=2,bg="#0099cc")
        SideEffectslb1.grid(row=6,column=2,padx=10,pady=5,sticky=W)
        SideEffectstxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable=SideEffects)
        SideEffectstxt.grid(row=6,column=3,padx=10,pady=5,sticky=E)

        MoreInformationlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="More Information",padx=2,bg="#0099cc")
        MoreInformationlb1.grid(row=7,column=2,padx=10,pady=5,sticky=W)
        MoreInformationtxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable=MoreInformation)
        MoreInformationtxt.grid(row=7,column=3,padx=10,pady=5,sticky=E)

        Medicationlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Medication",padx=2,bg="#0099cc")
        Medicationlb1.grid(row=8,column=2,padx=10,pady=5,sticky=W)
        Medicationtxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=25,textvariable=Medication)
        Medicationtxt.grid(row=8,column=3,padx=10,pady=5,sticky=E)

        TextPrescription=Text(Data_FrameRight,font=("arial",12,"bold"),width=55,height=17,padx=3,pady=5)
        TextPrescription.grid(row=0,column=0)

        TextPrescriptionData=Text(Data_Framedata,font=("arial",12,"bold"),width=203,height=12)
        TextPrescriptionData.grid(row=1,column=0)

        Prescriptionbtn=Button(Button_Frame,text="Precription",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=prescriptiondatafunc)
        Prescriptionbtn.grid(row=0,column=0,padx=15)

        Receiptbtn=Button(Button_Frame,text="Precription Data",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=prescriptiondata)
        Receiptbtn.grid(row=0,column=1,padx=15)

        Resetbtn=Button(Button_Frame,text="Reset",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=reesetfunc)
        Resetbtn.grid(row=0,column=2,padx=15)
        
        Deletebtn=Button(Button_Frame,text="Delete",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=deletefunc)
        Deletebtn.grid(row=0,column=3,padx=15)

        Exitbtn=Button(Button_Frame,text="Exit",bg="#ffaab0",activebackground="#fcceb2",font=("arial",15,"bold"),width=22,command=exitbtn)
        Exitbtn.grid(row=0,column=4,padx=15)

        Prescriptiondatarow=Label(Data_Framedata,bg="white",font=("arial",12,"bold"),text="Data\tReference Id\tPatient Name\tDate of Birth\tNHS Number\tTablet\t\tNo of Tablet\tIssue Date\tExpiry Date\tDaily Dose    Storage Advice  PatientID")
        Prescriptiondatarow.grid(row=0,column=0,sticky=W)

class Doctor():
    def __init__(self,root):
        self.root=root
        self.root.title=("Doctor Management System")
        self.root.geometry('1700x900+0+0')
        self.root.configure(background="black")

        Date_of_Registration=StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        DrId=StringVar()
        Drname=StringVar()
        DateofBirth=StringVar()
        Spes=StringVar()
        GovtPri=StringVar()
        Surgeries=StringVar()
        Experiences=StringVar()
        Nurses=StringVar()
        DrMobile=StringVar()
        PtName=StringVar()
        Apptime=StringVar()
        PtAge=StringVar()
        PatientAddress=StringVar()
        PtMobile=StringVar()
        Disease=StringVar()
        Case=StringVar()
        BenefitCard=StringVar()

        def exitbtn():
            exitbtn=tkinter.messagebox.askyesno("Doctor Management System","Are you sure you want to exit?")
            if(exitbtn>0):
               root.destroy()
               return
        def deletefunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return
        def resetfunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            return
        def Patient_idFunc():
            ranumber=random.randint(10000,999999)
            randomnumber=str(ranumber)
            DrId.set(randomnumber)
        def Prescriptiondatafunc():
            Patient_idFunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DrId.get()+"\t"
                                        +Drname.get()+"\t\t"+DateofBirth.get()+"\t\t"+Spes.get()+"\t\t"+GovtPri.get()+"\t\t"+
                                        Surgeries.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+
                                        PtName.get()+"\t\t"+Case.get()+"\t"+PtAge.get()+"\n")
            return
        
        def Prescriptionfunc():
            Patient_idFunc()
            TextPrescription.insert(END,"Date:\t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(END,"Patient Name:\t\t"+PtName.get()+"\n")
            TextPrescription.insert(END,"Appointment Timet:\t\t"+Apptime.get()+"\n")
            TextPrescription.insert(END,"Age:\t\t"+PtAge.get()+"\n")
            TextPrescription.insert(END,"Address:\t\t"+PatientAddress.get()+"\n")
            TextPrescription.insert(END,"Disease:\t\t"+Disease.get()+"\n")
            TextPrescription.insert(END,"Case:\t\t"+Case.get()+"\n")
            TextPrescription.insert(END,"Benefit Card:\t\t"+BenefitCard.get()+"\n")
            TextPrescription.insert(END,"Dr Mobile No:\t\t"+DrMobile.get()+"\n")
            return

        title=Label(self.root,text="Doctor Management System",font=("monotype corsiva",42,"bold"),bd=5,relief=GROOVE,bg="#b7d8d6",fg="black")
        title.pack(side=TOP,fill=X)

        Manage_Frame=Frame(self.root,width=1510,height=400,bd=5,relief=RIDGE,bg="#789e9e")
        Manage_Frame.place(x=10,y=80)

        Button_Frame=Frame(self.root,width=1510,height=55,bd=4,relief=RIDGE,bg="#eef3db")
        Button_Frame.place(x=10,y=460)

        Data_Frame=Frame(self.root,width=1510,height=270,bd=4,relief=RIDGE,bg="#eef3db")
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft=LabelFrame(Manage_Frame,width=1050,text="General Information",font=("arial",20,"italic bold"),height=390,bd=7,pady=1,relief=RIDGE,bg="#789e9e")
        Data_FrameLeft.pack(side=LEFT)

        Data_Framedata=LabelFrame(Data_Frame,width=1050,text="Doctor's Details",font=("arial",15,"italic bold"),height=390,bd=4,relief=RIDGE,bg="#3eb7bb")
        Data_Framedata.pack(side=LEFT)

        Data_FrameRight=LabelFrame(Manage_Frame,width=1050,text="Patient's Information",font=("arial",15,"italic bold"),height=390,bd=7,relief=RIDGE,bg="#789e9e")
        Data_FrameRight.pack(side=RIGHT)

        DrIdlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Doctor Id",bg="#789e9e")
        DrIdlb1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        DrIdtxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,state=DISABLED,textvariable=DrId)
        DrIdtxt.grid(row=0,column=1,padx=10,pady=5,sticky=E)

        DrNamelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Doctor Name",bg="#789e9e")
        DrNamelb1.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        DrNametxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Drname)
        DrNametxt.grid(row=1,column=1,padx=10,pady=5,sticky=E)

        DateofBirthlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date of Birth",bg="#789e9e")
        DateofBirthlb1.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        DateofBirthtxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=DateofBirth)
        DateofBirthtxt.grid(row=2,column=1,padx=10,pady=5,sticky=E)

        Speslb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Specialisation",bg="#789e9e")
        Speslb1.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        Spestxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Spes)
        Spestxt.grid(row=3,column=1,padx=10,pady=5,sticky=E)

        GovtPrilb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Govt/private",padx=2,bg="#789e9e")
        GovtPrilb1.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        GovtPricmb=ttk.Combobox(Data_FrameLeft,textvariable=GovtPri,width=25,state="readonly",font=("arial",12,"bold"))
        GovtPricmb['values']=("","Government","Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row=4,column=1,padx=10,pady=5,sticky=E)

        Surgerieslb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Surgeries",bg="#789e9e")
        Surgerieslb1.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        Surgeriestxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Surgeries)
        Surgeriestxt.grid(row=5,column=1,padx=10,pady=5,sticky=E)

        Experiencelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Experience",bg="#789e9e")
        Experiencelb1.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        Experiencetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Experiences)
        Experiencetxt.grid(row=6,column=1,padx=10,pady=5,sticky=E)

        Nurselb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Nurses under Dr",bg="#789e9e")
        Nurselb1.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        Nursetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Nurses)
        Nursetxt.grid(row=7,column=1,padx=10,pady=5,sticky=E)

        DrMobilelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Docter Mobile No",bg="#789e9e")
        DrMobilelb1.grid(row=8,column=0,padx=10,pady=5,sticky=W)
        DrMobiletxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=DrMobile)
        DrMobiletxt.grid(row=8,column=1,padx=10,pady=5,sticky=E)

        Datelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Date",padx=2,bg="#789e9e")
        Datelb1.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        Datetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Date_of_Registration)
        Datetxt.grid(row=0,column=3,padx=10,pady=5,sticky=E)

        PtNamelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Name",padx=2,bg="#789e9e")
        PtNamelb1.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        PtNametxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PtName)
        PtNametxt.grid(row=1,column=3,padx=10,pady=5,sticky=E)

        Apptimelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Appointment Time",padx=2,bg="#789e9e")
        Apptimelb1.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        Apptimetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Apptime)
        Apptimetxt.grid(row=2,column=3,padx=10,pady=5,sticky=E)

        PtAgelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Age",padx=2,bg="#789e9e")
        PtAgelb1.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        PtAgetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PtAge)
        PtAgetxt.grid(row=3,column=3,padx=10,pady=5,sticky=E)

        PtAddresslb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Address",padx=2,bg="#789e9e")
        PtAddresslb1.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        PtAddresstxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PatientAddress)
        PtAddresstxt.grid(row=4,column=3,padx=10,pady=5,sticky=E)

        PtMobilelb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Mobile No",padx=2,bg="#789e9e")
        PtMobilelb1.grid(row=5,column=2,padx=10,pady=5,sticky=W)
        PtMobiletxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=PtMobile)
        PtMobiletxt.grid(row=5,column=3,padx=10,pady=5,sticky=E)

        Diseaselb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Patient Disease",padx=2,bg="#789e9e")
        Diseaselb1.grid(row=6,column=2,padx=10,pady=5,sticky=W)
        Diseasetxt=Entry(Data_FrameLeft,font=("arial",12,"bold"),width=27,textvariable=Disease)
        Diseasetxt.grid(row=6,column=3,padx=10,pady=5,sticky=E)

        Caselb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Case",padx=2,bg="#789e9e")
        Caselb1.grid(row=7,column=2,padx=10,pady=5,sticky=W)
        Casecmb=ttk.Combobox(Data_FrameLeft,textvariable=Case,width=25,state="readonly",font=("arial",12,"bold"))
        Casecmb['values']=("","New Case","Old Case")
        Casecmb.current(0)
        Casecmb.grid(row=7,column=3,padx=10,pady=5,sticky=E)

        BenefitCardlb1=Label(Data_FrameLeft,font=("arial",12,"bold"),width=20,text="Benefit Card",padx=2,bg="#789e9e")
        BenefitCardlb1.grid(row=8,column=2,padx=10,pady=5,sticky=W)
        BenefitCardcmb=ttk.Combobox(Data_FrameLeft,textvariable=BenefitCard,width=25,state="readonly",font=("arial",12,"bold"))
        BenefitCardcmb['values']=("","Ayushman Card","Insurance","Pay Imedialtely","Pay when leaving")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row=8,column=3,padx=10,sticky=E)

        TextPrescription=Text(Data_FrameRight,font=("arial",12,"bold"),width=55,height=17,padx=3,pady=5)
        TextPrescription.grid(row=0,column=0)
        TextPrescriptionData=Text(Data_Framedata,font=("arial",12,"bold"),width=203,height=12)
        TextPrescriptionData.grid(row=1,column=0)

        Prescriptionbtn=Button(Button_Frame,text="Patient Information",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=Prescriptionfunc)
        Prescriptionbtn.grid(row=0,column=0,padx=15)

        DotorDetailbtn=Button(Button_Frame,text="Docter's Detail",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=Prescriptiondatafunc)
        DotorDetailbtn.grid(row=0,column=1,padx=15)

        Resetbtn=Button(Button_Frame,text="Reset",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=resetfunc)
        Resetbtn.grid(row=0,column=2,padx=15)
        
        Deletebtn=Button(Button_Frame,text="Delete",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=deletefunc)
        Deletebtn.grid(row=0,column=3,padx=15)

        Exitbtn=Button(Button_Frame,text="Exit",bg="#fe615a",activebackground="#cc6686",font=("arial",15,"bold"),width=22,command=exitbtn)
        Exitbtn.grid(row=0,column=4,padx=15)

        Prescriptiondatarow=Label(Data_Framedata,bg="white",font=("arial",12,"bold"),text="Date    Doctor ID    Doctor Name\tDate of Birth\tSpecialisation\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile No\tPatient Name\tCase\t Pt.Age  ")
        Prescriptiondatarow.grid(row=0,column=0,sticky=W)
if __name__=="__main__":
    main()