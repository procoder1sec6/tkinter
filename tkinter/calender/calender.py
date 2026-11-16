from tkinter import *
root = Tk()
root.geometry("600x600")
root.config(background="#1AFF01")
root.title("calender")

title = Label(root,text="calender",font=("Arial",80),bg="red",fg="brown")
title.grid(row=1,column=1)
enter = Label(root,text="Enter here: ",font=("Arial",60),bg="yellow",fg="black")
enter.grid(row=2,column=1,padx=0)
entry = Entry(root)
entry.grid(row=2,column=2)
root.mainloop()
