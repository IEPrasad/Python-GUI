

# -------- lesson 12----Tables - TreeView--------
''''
import tkinter as tk
from  tkinter import ttk

root = tk.Tk()

root.title('Tree View')
root.geometry('500x400')
root.resizable(False, False)

table = ttk.Treeview(root, columns=('name', 'age', 'email'), show='headings')
table.heading('name', text='Name')
table.heading('age', text='Age')
table.heading('email', text='Email')
table.column('age', width=100)
table.pack()

table.insert('', 0, values=('Kamal', 20, 'kamal23@gmail.com'))
table.insert('', 1, values=("Saman", 34, "Saman@gmail.com"))
table.insert('', 2, values=('Kumara', 54, 'Kuamara123@gmail.com'))
## if we have lot of detatils in a list we can't add those like this 
## because it is get more time 
## so let's see how to do this with for loop -------->>>


root.mainloop()

'''
# ---------- table tree with for loop ----------

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title('TreeView')
# root.geometry('500x400')
# root.resizable(False, False)

# table = ttk.Treeview(root, columns=('name', 'age', 'email'), show='headings')
# table.heading('name', text='Name')
# table.heading('age', text='Age')
# table.heading('email', text='Email')
# table.column('age', width=100)
# table.pack()

# name = ['Kamal', 'Saman', 'Pawan', 'Gayan', 'Yohani']
# age = [34, 45, 56, 44, 54]

# for idx, value in enumerate(name):
#   table.insert('', idx, values=(name[idx], age[idx], f'{name[idx]}@gmail.com'))


# root.mainloop()

# ---------------- now let's try to do another things with this--------


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('TreeView')
root.geometry('500x400')
root.resizable(False, False)

table = ttk.Treeview(root, columns=('name', 'age', 'email'), show='headings')
table.heading('name', text='Name')
table.heading('age', text='Age')
table.heading('email', text='Email')
table.column('age', width=100)
table.pack()

name = ['Kamal', 'Amal', 'Nishantha', 'Pawan']
age = [34, 64, 22, 54]

def selected_item(event):
  # print(table.selection())
  print(table.item(table.selection()))
  # label.configure(text=table.item(table.selection()))
  # label.configure(text=table.item(table.selection())['values'])
  label.configure(text=table.item(table.selection())['values'][0])
  # label.configure(text=table.item(table.selection())['values'][1])

for idx,value in enumerate(name):
  table.insert('', idx, values=(name[idx], age[idx], f'{name[idx]}@gmail.com'))

table.bind('<<TreeviewSelect>>', lambda event:selected_item(event))

label = ttk.Label(root)
label.pack()

root.mainloop()

# --------------- lesson 12 is over ------------















