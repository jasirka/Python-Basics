from tkinter import *
from tkinter import ttk

def action_login():
    print('Logged in successfully')

def login_form():
    root = Tk()
    root.title("Login form")
    root.geometry("1024x768")
    lbl_title = Label(root,text="Login Form Demo",fg="red",bg="yellow")
    lbl_title.pack()
    lbl_user = Label(root,text="Username",fg="blue")
    lbl_user.place(x=90,y=50)
    txt_user = Entry(width=30)
    txt_user.place(x=150,y=50)
    lbl_user = Label(root,text="Password",fg="blue")
    lbl_user.place(x=90,y=80)
    txt_pass = Entry(width=30)
    txt_pass.place(x=150,y=80)
    btn_login = Button(text="Login",fg="red",bg="light blue", command=action_login)
    btn_login.place(x=150,y=110)
    root.mainloop()

def window_demo():
    root = Tk()
    menu_bar = Menu(root)
    file = Menu(menu_bar)
    menu_bar.add_cascade(label="File",menu=file)
    file.add_command(label="Open",command=None)
    root.config(menu=menu_bar)


    canvas = Canvas(root, width=300, height=200, bg="light grey")
    canvas.pack(side="left")
    canvas.create_line(20,30,70,30)
    canvas.create_rectangle(40,50,150,90)
    photo = PhotoImage(file="mstore.png")
    lbl_image = Label(root,image=photo, width=100, height=100)
    lbl_image.pack()
    lbl_lang = Label(text="Languages",fg="red")
    lbl_lang.place(x=40,y=60)
    chk_1 = IntVar()
    chk_2 = IntVar()
    chk_eng = Checkbutton(root,text="English",variable=chk_1,onvalue=1,offvalue=0)
    chk_hin = Checkbutton(root,text="Hindi",variable=chk_2,onvalue=1,offvalue=0)
    chk_eng.place(x=120,y=60)
    chk_hin.place(x=180,y=60)
    lbl_gen = Label(root,text="Gender",fg="red")
    lbl_gen.place(x=40,y=100)
    rad_btn = StringVar(root,"1")
    rad_male = Radiobutton(root,text="Male",variable=rad_btn,value="1")
    rad_male.place(x=120,y=100)
    rad_female = Radiobutton(root,text="Female",variable=rad_btn,value="2")
    rad_female.place(x=180,y=100)
    lbl_gen = Label(root,text="Fruits",fg="red")
    lbl_gen.place(x=40,y=130)
    var_comb = StringVar(root,"please select")
    comb_fruits = ttk.Combobox(root,textvariable=var_comb,width=30,values="please select")
    comb_fruits['values'] = ("apple","orange","kiwi")
    comb_fruits.place(x=120,y=130)
    lbl_gen = Label(root,text="Programming",fg="red")
    lbl_gen.place(x=40,y=160)
    list_lang = Listbox(root,width=33,height=5)
    list_lang.place(x=120,y=160)
    list_lang.insert(0,"C++")
    list_lang.insert(1,"Python")
    list_lang.insert(2,"Java")



    root.mainloop()

# login_form()
window_demo()








