from tkinter import *
# def show_message():
#     print("Welcome to Python GUI!!")
# def open_gui():
#     root = Tk()
#     root.title("Python GUI")  # Set title of the page
#     root.geometry("1024x368") # Set the width and height of the window
#     lbl_welcome = Label(root, bg="yellow", fg="red", text="Welcome to GUI")
#     lbl_welcome.pack()
#     btn_action = Button(root, bg="green", fg="black", text="Click", command=show_message())
#     btn_action.place(x=500,y=200)
#     entry_name = Entry(root)
#     entry_name.place(x=500,y=150)
#     top_frame = Frame(root, width=50, height=50, bg="blue", relief="raised")
#     top_frame.pack(side=TOP, padx=300, pady=50)
#     root.mainloop()
# open_gui()

# def action_login():
#     print("Logged in successfully")
# Login form
# def login_form():
#     form = Tk()
#     form.title("Login Form Demo")
#     form.geometry("1024x768")
#     lbl_username = Label(form,fg="red",text="Username")
#     lbl_username.place(x=200,y=300)
#     txt_username = Entry(form)
#     txt_username.place(x=300,y=300)
#     lbl_password = Label(form,fg="red",text="Password")
#     lbl_password.place(x=200,y=350)
#     txt_password = Entry(form)
#     txt_password.place(x=300,y=350)
#     btn_submit = Button(form,fg="white",bg="blue",text="Login",command=action_login)
#     btn_submit.place(x=300,y=400)
#     form.mainloop()

# login_form()

# def create_shape():
#     shape = Tk()
#     canvas = Canvas(width=700, height=500, bg="blue")
#     canvas.pack(side="left")
    # canvas.create_line(30,120,300,350)
    # canvas.create_rectangle(100,150,400,350,fill="orange")
    # canvas.create_oval(100,150,400,350,fill="red")
    # shape.mainloop()

# create_shape()

# def upload_image():
#     root_image = Tk()
#     lbl_message = Label(root_image,text="Image Demo")
#     lbl_message.pack()
#     mypic = PhotoImage(file="demo_pic.png")
#     lbl_image = Label(root_image,image=mypic,width=700,height=500)
#     lbl_image.pack()
#     # root_image.geometry("1024x768")
#     root_image.mainloop()

# upload_image()

# def checkbox_demo():
#     root = Tk()
#     lbl_programming = Label(root,text="Programming")
#     lbl_programming.place(x=100,y=100)
#     checkbox1 = IntVar()
#     checkbox2 = IntVar()
#     check1 = Checkbutton(root, text="Java", variable=checkbox1, onvalue=1, offvalue=0)
#     check2 = Checkbutton(root, text="Python", variable=checkbox2, onvalue=1, offvalue=0)
#     check1.place(x=200,y=100)
#     check2.place(x=250,y=100)

#     lbl_programming = Label(root,text="Gender")
#     lbl_programming.place(x=200,y=200)
#     radiobutton = StringVar(root,"1")
#     radio1 = Radiobutton(root, text="Male", variable=radiobutton, value="1")
#     radio1.place(x=250,y=200)
#     radio2 = Radiobutton(root, text="Female", variable=radiobutton, value="2")
#     radio2.place(x=300,y=200)
#     root.mainloop()

# checkbox_demo()
# import tkinter as tk
# from tkinter import ttk
# def combobox_demo():
#     root = tk.Tk()
#     root.title("Combobox Demo")
#     var = tk.StringVar()
#     fruits = ttk.Combobox(root,width=27,textvariable=var)
#     fruits['values'] = ("Apple", "Orange", "Banana")
#     fruits.pack(pady=20)
#     fruits.current(2)
#     root.geometry("1064x768")
#     root.mainloop()

# combobox_demo()

# from tkinter.ttk import *

# def menu_demo():
#     root = Tk()
#     root.title("Menu Demo")

#     menubar = Menu(root)
#     file = Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="File", menu=file)
#     file.add_command(label="New File", command=None)
#     file.add_command(label="Open", command=None)
#     file.add_command(label="Save", command=None)
#     file.add_separator()
#     file.add_command(label="Exit", command=root.destroy)

#     edit = Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="Edit", menu=edit)
#     edit.add_command(label="Cut", command=None)
#     edit.add_command(label="Copy", command=None)
#     edit.add_command(label="Paste", command=None)
#     edit.add_command(label="Select all", command=None)
#     edit.add_separator()
#     edit.add_command(label="Find", command=None)
#     edit.add_command(label="Find again", command=None)

#     help = Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="Help", menu=help)
#     help.add_command(label="Help", command=None)
#     help.add_command(label="Demo", command=None)
#     help.add_separator()
#     help.add_command(label="About TTK", command=None)

#     root.config(menu=menubar)
#     root.mainloop()

# menu_demo()

# def checkbutton_demo():
#     root = Tk()
#     root.geometry("1064x768")
#     root.title("Checkbox Demo")
#     menu_button = Menubutton(root, text="Student")
#     menu_button.menu = Menu(menu_button, tearoff=0) 
#     menu_button["menu"] = menu_button.menu

#     var1 = IntVar()
#     var2 = IntVar()
#     var3 = IntVar()

#     menu_button.menu.add_checkbutton(label="Courses", variable=var1)
#     menu_button.menu.add_checkbutton(label="Students", variable=var2)
#     menu_button.menu.add_checkbutton(label="Careers", variable=var3)

#     menu_button.pack()
#     root.mainloop()

#Text Editor Demo

#from tkinter import messagebox

#creating root window
# root = Tk()

#function_definitions
# def callback():
#     text = textEditor.get(0.1,END)
#     print(text)

#defining text editor
# textEditor = Text(root, width=43, height=10)
# textEditor.pack()

# #button 1
# button1 = Button(root, text="Display Text", command = callback )
# button1.pack(pady=12)

# root.geometry('350x218')
# root.title("PythonLobby")
# root.mainloop()

#ScrollBar Demo

# text_editor = Text(root, width=15, height=14)
# text_editor.grid(row=0,column=0)

# scroll_bar = Scrollbar(root, orient=VERTICAL, command=text_editor.yview)
# scroll_bar.grid(row=0,column=1,sticky=N+S)
# text_editor.config(yscrollcommand=scroll_bar.set)
# root.title("Text Editor Demo")
# root.geometry("1024x768")
# root.mainloop()
root = Tk()
text_editor = Text(root, width=20, height=20, wrap=NONE)   # Need to set wrap to NONE for horizontal scroll
text_editor.grid(row=0,column=0)
scroll_bar = Scrollbar(root, orient=HORIZONTAL, command=text_editor.xview)
scroll_bar.grid(row=1,column=0,sticky=E+W)
text_editor.config(xscrollcommand=scroll_bar.set)
root.mainloop()


# ListBox Demo

# root = Tk()
# root.title("Listbox Demo")
# # root.geometry("1024*768")

# list_box = Listbox(root, width=50, height=30)
# list_box.place(x=300, y=100)
# # list_box.insert(0, "C")
# # list_box.insert(1, "C++")
# # list_box.insert(2, "Java")
# # list_box.insert(3, "Python")

# fruits = ["Apple", "Banana", "Orange", "Kiwi"]
# for item in fruits:
#     list_box.insert(END, item)
# root.mainloop()

