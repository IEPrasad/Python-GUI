from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)


img = PhotoImage(file='login.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

window.mainloop()



