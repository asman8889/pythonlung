from tkinter import *
from tkinter.messagebox import showinfo

def show_info():
    name = name_entry.get()
    amount = monney_entry.get()
    message = f"ชื่อ-นามสกุล: {name}\nจำนวนเงินเก็บ: {amount}"
    showinfo(title="ข้อมูลที่กรอก", message=message)

GUI = Tk()
GUI.geometry("500x400")
GUI.title("โปรแกรมเก็บเงิน")


bg_color = "#B2BEB5"
GUI.configure(bg=bg_color)


title_label = Label(GUI, text="โปรแกรมเก็บเงิน", font=("Arial", 24, "bold"), fg="#F5FFFA", bg=bg_color)
title_label.pack(pady=20)


entry_bg_color = "#E5E5E5"
entry_width = 20
entry_height = 2

name_label = Label(GUI, text="ชื่อ-นามสกุล:", font=("Arial", 12), fg="#2F4F4F", bg=bg_color)
name_entry = Entry(GUI, width=entry_width, font=("Arial", 12), bg=entry_bg_color, relief=GROOVE)
monney_label = Label(GUI, text="จำนวนเงินเก็บ:", font=("Arial", 12), fg="#2F4F4F", bg=bg_color)
monney_entry = Entry(GUI, width=entry_width, font=("Arial", 12), bg=entry_bg_color, relief=GROOVE)
button = Button(GUI, text="แสดงข้อมูล", font=("Arial", 12, "bold"), bg="#008B8B",
                 fg="#F5FFFA", activebackground="#F5FFFA",
                   activeforeground="#008B8B", command=show_info)

name_label.place(relx=0.5, rely=0.4, anchor=CENTER)
name_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
monney_label.place(relx=0.5, rely=0.6, anchor=CENTER)
monney_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
button.place(relx=0.5, rely=0.85, anchor=CENTER)

GUI.mainloop()
