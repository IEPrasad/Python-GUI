
        # Python GUI - Tutorial-3 |variables|

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('variables')
root.geometry('400x300')


# let's create variable like this 
    ## we create tk.StringVar()
                #  tk.BooleanVar()
                #     -----
                #     ----
# variable_value = tk.StringVar()

# if we want we can put a value here
variable_value = tk.StringVar(value='Welcome')


label1 = ttk.Label(root,textvariable=variable_value)
label1.pack()

entry1 = ttk.Entry(root,textvariable=variable_value)
entry1.pack()

## 2 now try to create a button
# button1 = ttk.Button(root, text="Click ME", command=lambda:print(entry1.get()))
        ## if we want to get varible value we can do it like this
button1 = ttk.Button(root,text="Click ME", command=lambda:print(variable_value.get()))
button1.pack()


root.mainloop()





