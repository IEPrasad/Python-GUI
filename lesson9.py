'''


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Lesson 9-|Slider and Progress bar|')
root.iconbitmap("icon.ico")
root.geometry('400x300')
root.resizable(False, False)

# scale = ttk.Scale(root, command=lambda value:print(value))
# scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100, length=400)
scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100, length=200, orient='vertical')
scale.pack()

root.mainloop()

'''

'''
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Lesson 9-|Slider and Progress bar|')
root.iconbitmap("icon.ico")
root.geometry('400x300')
root.resizable(False, False)

# scale_value = tk.DoubleVar()
## if we want to change the start value we can give the value through our variable
scale_value = tk.DoubleVar(value=50)


scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100, length=200, variable=scale_value)
scale.pack()

root.mainloop()
'''
    # Now we talked aboved the scale bar 
    #     let's see how to create a progress bar
# -----------------------------------

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Progress bar with scale bar')
root.geometry('300x200')
root.resizable(False, False)
root.iconbitmap('icon.ico')

scale_value = tk.DoubleVar(value=50)

scale = ttk.Scale(root, command=lambda value:print(value), from_=0, to=100, length=250, variable=scale_value)
scale.pack()


progressbar = ttk.Progressbar(root, value=50, variable=scale_value, length=200)
# progressbar = ttk.Progressbar(root, value=50, variable=scale_value, length=200, orient='vertical')
progressbar.pack()

root.mainloop()


# ------------ lesson 9 is over ----------------------










