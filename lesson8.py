
      # Python GUI - 08 | SpinBox |
'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('SpinBox-lesson-8')
root.geometry('300x200')
root.resizable(False, False)

spinbox_value = tk.StringVar()

# spinbox = ttk.Spinbox(root, values=[1,2,3,4,5,6,7,8,9,10], textvariable=spinbox_value)
# we can give the value like this 
# spinbox = ttk.Spinbox(root, from_=5, to = 15, textvariable=spinbox_value)

## and we can change the rcrement
spinbox = ttk.Spinbox(root, from_=5, to=15, increment=2, textvariable=spinbox_value)
spinbox.pack()

label = ttk.Label(root, textvariable=spinbox_value)
label.pack()

root.mainloop()
'''


import tkinter as tk
from tkinter import ttk
from calendar import month_name

root = tk.Tk()

root.title('MonthNames-lesson8')
root.resizable(False, False)
root.geometry('300x200')

selected_month = tk.StringVar()

month_names = [month_name[i] for i in range(1,13)]

spinbox = ttk.Spinbox(root, values=month_names, textvariable=selected_month)
spinbox.pack()

label = ttk.Label(root, textvariable=selected_month)
label.pack()

root.mainloop()


------------- lesson 8 is over -------------







