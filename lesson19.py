
        # Python GUI - 19 | Message Box | 

# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# root = tk.Tk()
# root.title('Message boxes')
# root.geometry('500x400')

# def open_messagebox():
#   # messagebox.showerror('Error title', 'This is a error')
#   result = messagebox.showerror('Error title', 'This is a error')
#   print(result)
  
#   ## there is showerror, showinfo, showwarning

# button = ttk.Button(root, text='Click Me', command=open_messagebox)
# button.pack()


# root.mainloop()


# ----------------



# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# root = tk.Tk()
# root.title('Message boxes')
# root.geometry('500x400')

# def open_messagebox():
#   result = messagebox.askquestion('Error title', 'Are you sure?')
#   print(result)

#     # askokcancel
#     # askquestion
#     # askretrycancel
#     # askyesno
#     # askyesnocancel


# button = ttk.Button(root, text='Click Me', command=open_messagebox)
# button.pack()


# root.mainloop()

# -----------

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('Message boxes')
root.geometry('500x400')

def open_messagebox():
  result = messagebox.askokcancel('This is a title', 'This is a message')
  print(result)
  if result:
    print('Click OK')
  else:
    print('Click Cancel')




button = ttk.Button(root, text='Click Me', command=open_messagebox)
button.pack()


root.mainloop()


# ---------- the lesson 19 is over ---------








