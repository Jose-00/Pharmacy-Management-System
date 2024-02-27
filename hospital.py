import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
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

if __name__=="__main__":
    root=Tk()
    app=Hospital(root)
    root.mainloop()

