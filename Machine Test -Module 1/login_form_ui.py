from tkinter import *

def login_action():
    print("Logged in successfully")

def login_form():
    root = Tk()
    root.title("Login form UI")
    root.geometry("1024x768")
    lbl_main_text = Label(text="Login Form UI",fg="red")
    lbl_main_text.pack()
    lbl_username = Label(text="Username",fg="grey")
    lbl_username.place(x=30,y=50)
    txt_username = Entry(width=30)
    txt_username.place(x=90,y=50)
    lbl_password = Label(text="Password",fg="grey")
    lbl_password.place(x=30,y=70)
    txt_password = Entry(width=30)
    txt_password.place(x=90,y=70)
    btn_login = Button(text="Login",fg="red",bg="blue",command=login_action)
    btn_login.place(x=90,y=100)
    root.mainloop()

login_form()