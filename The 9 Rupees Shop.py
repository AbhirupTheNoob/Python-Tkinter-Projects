from tkinter import *

root=Tk()
root.title("The 9 Rupees Shop")
root.geometry("800x600")
root.config(background='white')

def calculate_bill():
    k=e1.get()
    s=e2.get()
    j=e3.get()
    total=((int(k)*9)+(int(s)*9)+(int(j)*9))
    label8=Label(root,text="Rs."+str(total),font=("Times New Roman",25,"bold"),bg="white",fg="red")
    label8.place(x=275,y=375)

#----------------------------Menu Section--------------------------------------------------
label1=Label(root,text="Menu",font=("Times New Roman",28,"bold"),bg="white",fg="blue")
label1.place(x=50,y=0)

label2=Label(root,text="1. Kachori   Rs.9/pc",font=("Times New Roman",20,"bold"),bg="white",fg="green")
label2.place(x=50,y=50)

label3=Label(root,text="2. Samosa    Rs. 9/pc",font=("Times New Roman",20,"bold"),bg="white",fg="green")
label3.place(x=50,y=100)

label4=Label(root,text="3. Jalebi      Rs.9/pc",font=("Times New Roman",20,"bold"),bg="white",fg="green")
label4.place(x=50,y=150)

label4=Label(root,text="-----------------------------------x------------------------------------",font=("Times New Roman",20,"bold"),bg="white",fg="green")
label4.place(x=50,y=200)
#-------------------------------Billing Section--------------------------------------------
label5=Label(root,text="Kachori Amount",font=("Times New Roman",15,"bold"),bg="white",fg="black")
label5.place(x=50,y=250)
e1=Entry(root,justify="center",font=("Calibri",15,"bold"))
e1.place(x=50,y=275)

label6=Label(root,text="Samosa Amount",font=("Times New Roman",15,"bold"),bg="white",fg="black")
label6.place(x=270,y=250)
e2=Entry(root,justify="center",font=("Calibri",15,"bold"))
e2.place(x=270,y=275)

label7=Label(root,text="Jalebi Amount",font=("Times New Roman",15,"bold"),bg="white",fg="black")
label7.place(x=500,y=250)
e3=Entry(root,justify="center",font=("Calibri",15,"bold"))
e3.place(x=500,y=275)

button=Button(root,text="Total Amount",font=("Calibri",15,"bold"),fg="white",bg="green",command=calculate_bill)
button.place(x=275,y=325)


root.mainloop()
