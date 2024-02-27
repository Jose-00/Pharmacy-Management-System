import random
import time
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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
    root=Tk()
    app=Doctor(root)
    root.mainloop()