

        # --------------Python GUI - 06 | Radio Buttons |-------------

  # ** Checkboxes and Radio buttons are both types of GUI elements used for user input in 
  #   graphical user interfaces, but they have different charateristics and use cases:

  #   1: Chekbox:

  #         ** A checkbox is a GUI element that allows users to select or deselect and  
  #             option independently.
          
  #         ** You can have multiple checkboxes in a group, and users can choose any 
  #             combination of options.
          
  #         ** Each checkbox is typically independent of others in the group.
          
  #         ** Checkboxes are suitable when users can choose multiple options simultaneously.


  #   2: Radio Buttons:

  #         ** A radion button, or option button, is a GUI element that presents a set of
  #         mutually exclusive options.

  #         ** Users can choose only one option from the group of radio buttons.

  #         ** When one radion button in a group is selected, it automatically deselecteds
  #             any other radio button in the same group.

  #         ** Radio buttons are suitable when users need to make a single selection
  #             from a set of options.

  # In summary, checkboxes are used when users can make multiple selections from a group 
  # of options, while radio buttons are used when users need to make a single, exclusive   
  # selection from a set of options. The choice between checkboxes and radio buttons depends
  # on the specific requirements of the user interface and the type of input you want to 
  # collect from the user.

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title('Radion Buttons')
# root.geometry('300x200')
# root.resizable(False, False)

# radio1 = ttk.Radiobutton(root, text='Python')
# radio1.pack()

# radio2 = ttk.Radiobutton(root, text='Java')
# radio2.pack()

# radio3 = ttk.Radiobutton(root, text= 'C++')
# radio3.pack()

# root.mainloop()

#### above we create the three radion buttons but there is a problem 
  # if we click the one radion button when all are select automatically .....
  ## for doing this we have to separate these all are from each other .....
  ## for this we have to give the value for that....


# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title('Radion Buttons')
# root.geometry('300x200')
# root.resizable(False, False)

# radio1 = ttk.Radiobutton(root, text='Python', value='Python')
# radio1.pack()

# radio2 = ttk.Radiobutton(root, text='Java', value='Java')
# radio2.pack()

# radio3 = ttk.Radiobutton(root, text= 'C++', value='C++')
# radio3.pack()

# root.mainloop()

## now we solve this problem 
  ## now let's see how to add variables for that..........



import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Radion Buttons')
root.geometry('300x200')
root.resizable(False, False)

radio_var = tk.StringVar()


def select_radio():
  label.configure(text=radio_var.get())

radio1 = ttk.Radiobutton(root, text='Python', value='Python', variable=radio_var, command=select_radio)
radio1.pack()

radio2 = ttk.Radiobutton(root, text='Java', value='Java', variable=radio_var, command=select_radio)
radio2.pack()

radio3 = ttk.Radiobutton(root, text= 'C++', value='C++', variable=radio_var, command=select_radio)
radio3.pack()

label = ttk.Label(root)
label.pack()

root.mainloop()


# ----------------- lesson 6 is over --------------
