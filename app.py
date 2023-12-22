import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('ToDo App')
root.geometry('400x500')
root.resizable(False, False)
root.iconbitmap('icon.ico')

task_list = []

def add_task(event):
  task = task_entry.get()
  task_entry.delete(0, tk.END)
  if task:
    with open('tasklist.txt', 'a') as file:
      file.write(f'\n{task}')
    listbox.insert(tk.END, task)
    task_list.append(task)

def delete_task():
  task = listbox.get(tk.ANCHOR )
  listbox.delete(tk.ANCHOR)
  task_list.remove(task)
  with open('tasklist.txt', 'w') as file:
    for task in task_list:
      file.write(f'\n{task}')


def open_tasks():
  with open('tasklist.txt', 'r') as file: 
    tasks = file.readlines()
    
  for task in tasks:
    if task != '\n':
      listbox.insert(tk.END, task)
      task_list.append(task )
    


heading = ttk.Label(root, text='ALL TASKS', font='arial 20 bold')
heading.pack(pady=8)

frame = ttk.Frame(root, width=400, height=50)
frame.pack(pady=18)

task_entry = ttk.Entry(frame, font='arial 18', width=24)
task_entry.pack()

task_entry.bind('<Return>', add_task)

frame1 = ttk.Frame(root, width=300, height=250)
frame1.pack(pady=8)

listbox = tk.Listbox(frame1, font='arial 12', width=35, height=14)
listbox.pack()

open_tasks()


s = ttk.Style()
s.configure('TButton', font='arial 12')


delete_btn = ttk.Button(root, text='Delete', style='TButton', command=delete_task)
delete_btn.pack(side='bottom', pady='12', ipadx=8, ipady=12)



root.mainloop()
