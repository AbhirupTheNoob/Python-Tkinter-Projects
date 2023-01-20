import tkinter
from tkinter import *
from tkinter.font import BOLD
from textblob import TextBlob


root=Tk()
root.title("Spelling Checker")
root.geometry("800x600")
root.config(background='white')

def check_spell():
    word=enter_text.get()
    b=TextBlob(word)
    right_word=str(b.correct())

    c=Label(root,text="Correct English Spelling Is: ",font=("Calibri",20),bg='white',fg='red')
    c.place(x=150,y=250)
    spelling.config(text=right_word)


heading=Label(root,text="Spelling Checker",font=("Times New Roman",30,BOLD),bg='white',fg='blue')
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width="30",font=("Calibri",25),bg='white',border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="Check",font=("Calibri",20,"bold"),fg="white",bg="green",command=check_spell)
button.pack()

spelling=Label(root,font=("Calibri",20),bg="white",fg="red")
spelling.place(x=450,y=250)
root.mainloop()