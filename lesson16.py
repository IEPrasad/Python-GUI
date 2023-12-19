
      # Python GUI - 16 | Layouts |

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('Lyaouts')
# root.geometry('500x400')

# hello_label = ttk.Label(root, text='Hello', background='orange')
# welcome_label = ttk.Label(root, text='Welcome', background='yellow')

# hello_label.pack()
# welcome_label.pack()


# root.mainloop()   

# ----------

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('Lyaouts')
# root.geometry('500x400')

# hello_label = ttk.Label(root, text='Hello', background='orange')
# welcome_label = ttk.Label(root, text='Welcome', background='yellow')

# # hello_label.pack(side='left')
# # hello_label.pack(side='left', expand=True)
# hello_label.pack(side='left', expand=True, fill="both")
# welcome_label.pack()


# root.mainloop()   

# ----------------

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('Lyaouts')
# root.geometry('500x400')

# hello_label = ttk.Label(root, text='Hello', background='orange')
# welcome_label = ttk.Label(root, text='Welcome', background='yellow')

# # hello_label.pack()
# # welcome_label.pack()

# root.columnconfigure(0)
# root.columnconfigure(1)
# root.columnconfigure(2)
# root.rowconfigure(0)
# root.rowconfigure(1)

# # hello_label.grid(row=1, column=1)
# hello_label.grid(row=1, column=1, sticky='nsew')
# welcome_label.grid(row=0, column=2, sticky='nsew')


# root.mainloop()

# -----------------------



# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('Lyaouts')
# root.geometry('500x400')

# hello_label = ttk.Label(root, text='Hello', background='orange')
# welcome_label = ttk.Label(root, text='Welcome', background='yellow')

# # hello_label.pack()
# # welcome_label.pack()

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)

# # hello_label.grid(row=1, column=1)
# hello_label.grid(row=1, column=1, sticky='nsew')
# welcome_label.grid(row=0, column=2, sticky='nsew')


# root.mainloop()

# ---------------------


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Lyaouts')
root.geometry('500x400')

hello_label = ttk.Label(root, text='Hello', background='orange')
welcome_label = ttk.Label(root, text='Welcome', background='yellow')

# hello_label.place(x=100, y=100)
hello_label.place(x=100, y=100, height=100, width=300)

# welcome_label.place(relx=0, rely=0)
# welcome_label.place(relx=0.1, rely=0.1)
welcome_label.place(relx=0.1, rely=0.2, width=100, height=0.1)

###$$ for the plae relativex = relx; you can give the value
### between 0 and 1

root.mainloop()

# ---------------

# we  discussed these
#       dfj_label.pack
#       dfj_label.grid
#       dfj_label.



