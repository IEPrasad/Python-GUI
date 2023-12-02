
'''
import tkinter as tk

root = tk.Tk()

root.title('Hello World!')

root.iconbitmap('icon.ico')

# root.geometry('400x400')
# or 
height, width = 400, 400
# root.geometry(f'{width}x{height}')

root.geometry(f'{width}x{height}+200+100')

root.resizable(False, False)

root.mainloop()
'''
# --------------- lesson 1 is done -----------------

# Lesson 2---->>> Entry fields, button, label

import tkinter as tk
from tkinter import ttk


# root = tk.Tk()

# root.title('Lesson - 2|Basic Widgets|')
# root.geometry('400x400')

# button_1 = tk.Button(root, text='Type 1 button with tk')
# button_1.pack()
# ## this is type-1 button

# button_2 = ttk.Button(root, text='Type 2 button with ttk')
# button_2.pack()


# entry_1 = tk.Entry(root,text='tk entry field')
# entry_1.pack()

# entry_2 = ttk.Entry(root)
# entry_2.pack( )


# label_1 = tk.Label(root, text='this is the tk label')
# label_1.pack()

# label_2 = ttk.Label(root, text='this is the ttk label')
# label_2.pack()


# root.mainloop()

# -----------

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('This is the practice')
root.geometry('400x400')
root.iconbitmap('icon.ico')

def button_click_func():
  entry_field_value = entry_1.get()
  label_1.configure(text='My name is: '+entry_field_value)

button_1 = tk.Button(root, text='Button1,1',command=button_click_func)
button_1.pack()

# button_2 = ttk.Button(root, text='Button2,2')
# button_2.pack()

entry_1 = tk.Entry(root)
entry_1.pack()



# entry_2 = ttk.Entry(root)
# entry_2.pack()

label_1 = tk.Label(root)
label_1.pack()

# label_2 = ttk.Label(root)
# label_2.pack()
# label_2.configure(text='this is the label')


root.mainloop()

# ----------- lesson 2 is over -------------









