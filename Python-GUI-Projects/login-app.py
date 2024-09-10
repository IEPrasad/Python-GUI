from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

# Load image (make sure 'login.png' exists in the directory)
img = PhotoImage(file='login.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

# Corrected color code for heading
heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=30)  # Added placement for heading

# User entry
user = Entry(frame, width=25, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)

# Frame for user entry underline
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

window.mainloop()
