from tkinter import Tk, Frame, Label, Entry, Button, Canvas, PhotoImage, END

def on_focus_in(event):
    widget = event.widget
    if widget.get() == placeholders[widget]:
        widget.delete(0, END)
        widget.config(fg='black')
        if widget == txt_pass:
            widget.config(show='*')

def on_focus_out(event):
    widget = event.widget
    if not widget.get():
        widget.insert(0, placeholders[widget])
        widget.config(fg='grey', show='')

def upload_image(canvas,image,x,y):
    try:
        upload_image = PhotoImage(file=image)
        canvas.create_image(x, y, image=upload_image)
        canvas.image = upload_image  # Prevent garbage collection
    except Exception as e:
        print("Error loading image:", e)

root = Tk()
root.geometry("1024x768")

login_frame = Frame(root, bd=1, background="light grey", padx=20, pady=20, relief="ridge", height=330, width=300)
login_frame.pack(pady=5)
login_frame.pack_propagate(False)

label_insta = Label(login_frame, text="Instagram", font=("Bahnschrift SemiLight Condensed", 16, "bold"), fg="white", width=30, height=1, bg="light grey")
label_insta.pack(pady=10)

txt_user = Entry(login_frame, fg='light grey', width=35)
txt_pass = Entry(login_frame, fg='light grey', width=35)

placeholders = {
    txt_user: "Phone number, username or email",
    txt_pass: "Password"
}

txt_user.insert(0, placeholders[txt_user])
txt_pass.insert(0, placeholders[txt_pass])

txt_user.bind("<FocusIn>", on_focus_in)
txt_user.bind("<FocusOut>", on_focus_out)
txt_pass.bind("<FocusIn>", on_focus_in)
txt_pass.bind("<FocusOut>", on_focus_out)

txt_user.pack(padx=10, pady=10)
txt_pass.pack(padx=10, pady=3)

button = Button(login_frame, text="Log in", width=34, height=1, bg="#4db5f9", fg="white", font=("Bahnschrift SemiLight Condensed", 9, "bold"), relief="ridge")
button.pack(pady=10)

login_canvas = Canvas(login_frame, width=200, height=120, bg="light grey", border=0, highlightthickness=0)
login_canvas.pack()
login_canvas.create_line(0, 15, 80, 15, fill="white")
login_canvas.create_text(95, 15, text="OR", font=("Bahnschrift SemiLight Condensed", 12, "bold"), fill="white")
login_canvas.create_line(110, 15, 200, 15, fill="white")
upload_image(login_canvas,"fb-icon.png",40,70)

login_canvas.create_text(110,70, text="Login with Facebook")
login_canvas.create_text(110,100, text="Forgot password?")

signup_frame = Frame(root, bd=1, background="light grey", padx=60, pady=10, relief="ridge", height=150, width=350)
signup_frame.pack()
lbl_signup_qn = Label(signup_frame, text="Don't have an account?",fg="white", font=("Bahnschrift SemiLight Condensed", 12),bg="light grey")
lbl_signup_qn.pack(side="left")
lbl_signup = Label(signup_frame, text="Sign up",fg="blue", font=("Bahnschrift SemiLight Condensed", 12, "bold"),bg="light grey")
lbl_signup.pack(side="left")
app_frame = Frame(root, bd=0, background="light grey", pady=5, relief="ridge", height=50, width=250)
app_frame.pack()
lbl_app = Label(app_frame, text="Get the app.", padx=120, bg="light grey")
lbl_app.pack()
gpay_canvas = Canvas(app_frame, width=150, height=40, bd=0, bg="light grey")
gpay_canvas.pack(side="left")
upload_image(gpay_canvas,"gpay.png",90,20)
mstore_canvas = Canvas(app_frame, width=150, height=40, bd=0, bg="light grey")
mstore_canvas.pack(side="right")
upload_image(mstore_canvas,"mstore.png",60,20)
root.mainloop()
