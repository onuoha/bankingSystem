from tkinter import *
import os
from PIL import ImageTk, Image

# Main Screen
main = Tk()
main.title('Banking App')

# Functions

def finish_reg():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name=="" or age==""or gender=="" or password=="":
        notif.config(fg="red", text="All fields required * ")
        return
    
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red", text="Account already exists")
            return
        else:
            new_file = open(name, "w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.close()
            notif.config(fg="green", text="Account has been created")
def register():
    # Variable definition
    global temp_name
    global temp_age
    global temp_password
    global temp_gender
    global notif

    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    # Registration window
    register_screen = Toplevel(main)
    register_screen.title('Register')
    Label(register_screen, text="Fill in your details to register", font=('Calibri', 12)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text="Name", font=('Calibri', 12)).grid(row=1, sticky=W)
    Label(register_screen, text="Age", font=('Calibri', 12)).grid(row=2, sticky=W)
    Label(register_screen, text="Gender", font=('Calibri', 12)).grid(row=3, sticky=W)
    Label(register_screen, text="Password", font=('Calibri', 12)).grid(row=4, sticky=W)
    notif = Label(register_screen, font=('Calibri', 12))
    notif.grid(row=6, sticky=W)

    # Registration entries
    Entry(register_screen, textvariable=temp_name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_password, show="*").grid(row=4, column=0)

    # Buttons
    Button(register_screen, text='Register', command=finish_reg, font=('Calibri', 12)).grid(row=5, sticky=N,pady=10)
def login():
    pass

# Image
img = Image.open("bankingSystem/images/bank.jpg")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

# Labels
Label(main, text = "CEOT eBank Beta", font=('Calibri', 14)).grid(row=0, sticky=N, pady=10)
Label(main, text = "The most secure and reliable African Bank...", font=('Calibri', 11)).grid(row=1, sticky=N)
Label(main, image=img).grid(row=2, sticky=N, pady=15)

# Buttons
Button(main, text="Register", font=('Calibri', 12), width=20, command=register).grid(row=3, sticky=N)
Button(main, text="Login", font=('Calibri', 12), width=20, command=login).grid(row=4, sticky=N, pady=10)
main.mainloop()