
                # Python GUI - 10 | Event Binding |
  #       ** In Python GUI programming, event binding refers to the process of conecting 
  #       functions or methods to specific events. These events include actions like
  #       button clicks, mouse movements, key presses, and more. Event binding allows
  #       developers to associate custom code (callbacks or handlers) with these events,
  #       enabling the program to respond to user action.

  # Here's a brief overview:

# 1. GUI Elements and Events:
#       ** GUI elements such as buttons, text fields, and sliders can generate events
#       when users interact with them.

#       ** Events include actions like button clicks, mouse movements, key presses, etc.

# 2. Event Binding:
#       ** Event binding involves associating a function or method with a specific event 
#       for a particular GUI element.
      
#       ** When the associate event occurs, the bound function is executed. 
  
# 3. Example: Button Click Event:
#       ** Suppose you have a GUI button, and you want a function to run when the 
#       button is clicked.

#       ** You bind a function to the button's click event, so the function is 
#       triggered when the button is pressed.
# -------------------------------------


# import tkinter as tk 
# from tkinter import ttk

# root = tk.Tk()

# root.title('Events')
# root.geometry('300x200')
# root.resizable(False, False)

# btn = ttk.Button(root, text='Click Me')
# btn.pack()

# root.bind('<Key>', lambda event:print("Hello"))

# root.mainloop()

# ---------

# import tkinter as tk 
# from tkinter import ttk

# root = tk.Tk()

# root.title('Events')
# root.geometry('300x200')
# root.resizable(False, False)

# btn = ttk.Button(root, text='Click Me')
# btn.pack()

# btn.bind('<Key>', lambda event:print("Hello"))

# root.mainloop()

# ---------------------

## now click the button and press any key after that
# you can see the Hello on cmd  

# If we want to see what key pressed we we can
# change this code like this 

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title('Events')
# root.geometry('300x200')
# root.resizable(False, False)

# btn = ttk.Button(root, text="Click Me")
# btn.pack()

# btn.bind('<Key>', lambda event:print(event))

# root.mainloop()

# ---------------------
# Now let's see how to join our mouse

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title('Events')
# root.geometry('300x200')
# root.resizable(False, False)

# btn = ttk.Button(root, text="Click Me")
# btn.pack()

# # btn.bind('<Motion>', lambda event:print(event))
# root.bind('<Motion>', lambda event:print(event))

# root.mainloop()

# ------------

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title('Events')
# root.geometry('300x200')
# root.resizable(False, False)

# btn = ttk.Button(root, text="Click Me")
# btn.pack()

# # root.bind('<Enter>', lambda event:print("Enter to window"))
# # root.bind('<Leave>', lambda event:print("Leave from window"))

# btn.bind('<Enter>', lambda event:print("Enter to button"))
# btn.bind('<Leave>', lambda event:print("Leave from button"))

# root.mainloop()

# -------------------
    # Let's see another thing


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Events')
root.geometry('300x200')
root.resizable(False, False)

btn = ttk.Button(root, text="Click Me")
btn.pack()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<FocusIn>', lambda event:print('Entry field selected'))
entry.bind('<FocusOut>', lambda event:print('Entry field deselected'))

root.mainloop()

# ------------- lesson 10 is over 
                    # but Python GUI event is not over ------------ 




