from tkinter import *
import time
from tkinter import messagebox
root = Tk()
root.title("Log-In")
root.config(bg="white")#default
root.geometry("300x280")

def exit():
    messagebox.showinfo("Exit","You are going to finish the program!")
    time.sleep(1)
    root.destroy()
welc_label=Label(text="Log-In Page",bg="cyan",fg="green")
empty = Label(text="",bg="white",fg="white")
empty1 = Label(text="",bg="white",fg="white")
empty2 = Label(text="",bg="white",fg="white")
empty3 = Label(text="",bg="white",fg="white")
empty4 = Label(text="",bg="white",fg="white")
empty5 = Label(text="",bg="white",fg="white")
exit_button = Button(text="Exit",fg="red",command=exit)
username = Entry()
username.insert(0,"Enter your username...")
username.focus()
password = Entry()
password.insert(0,"Enter your password...")
def submit():
    username_value = username.get()
    password_value = password.get()
    root.destroy()
    window = Tk()
    window.title("User's Info's")
    window.geometry("400x400")
    window.config(bg="cyan")
    username_label = Label(text="Username: {}".format(username_value))
    password_label = Label(text="Password: {}".format(password_value))
    username_label.pack()
    password_label.pack()
submit_button = Button(text="Submit",fg="green",command=submit)
    
welc_label.pack()
empty.pack()
empty1.pack()
empty2.pack()
username.pack()
empty3.pack()
password.pack()
empty4.pack()
exit_button.pack(side=LEFT)
submit_button.pack(side=RIGHT)
root.mainloop()