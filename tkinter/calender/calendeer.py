from tkinter import *
import calendar
def create():
    c = Tk()
    c.geometry("800x800")
    c.config(backgroud="#0077FF")
    c.title("calender")
    y = int(entry.get())
    c_storage = calendar.calendar(y)
    c_text = Label(c,text=c_storage,font=("Arial",20))
    c_text.grid(row=1,column=1)
    c.mainloop()

root = Tk()
root.geometry("600x600")
root.config(background="#1AFF01")
root.title("calender maker")

title = Label(root,text="calender",font=("Arial",80),bg="red",fg="brown")
title.grid(row=1,column=1)
enter = Label(root,text="Enter here: ",font=("Arial",60),bg="yellow",fg="black")
enter.grid(row=2,column=1,padx=0)
entry = Entry(root)
entry.grid(row=2,column=2)
calculate = Button(root,text="calculate",font=("Arial",40),command=create)
calculate.grid(row=3,column=1)
root.mainloop()
