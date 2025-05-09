from tkinter import *

def btn_action(event):
    btn_text = event.widget.cget("text")
    if btn_text == "=":
        try:
            result = str(eval(entry_text.get()))
            # entry_text.delete(0, END)
            entry_text.insert(END, "="+result)
        except Exception:
            print("Error!!")
    elif btn_text == "C":
        entry_text.delete(0, END)
    else:
        entry_text.insert(END, btn_text+" ")

root = Tk()
root.geometry("300x300")

entry_text = Entry(root)
entry_text.pack(fill=Y, padx=10, pady=10)

btn_list = [ 
    ["7","8","9","+"],
    ["6","5","4","-"],
    ["3","2","1","*"],
    ["C","0","=","/"],
]

frame = Frame(root)
frame.pack()

for btn_row in btn_list:
    btn_frame = Frame(frame)
    btn_frame.pack(fill=BOTH)
    for btn in btn_row:
        button = Button(btn_frame,text=btn, relief=RAISED, bg="light blue", width=2)
        button.pack(side=LEFT, padx=4, pady=4)
        button.bind("<Button-1>", btn_action)

root.mainloop()
