
        # Python GUI -17 | Toggle Button |

# In python, GUI development can be done using various libraries, and one popular choice is Tkinter. 
# Tkinter is a built-in module that comes with Python and provides tools for creating graphical user interfaces.

# A toggle button, also known as a check button or checkbox, is a GUI element that can be in either 
# an "on" or "off" state. Users can toggle the button switch between these states.

# Here's a simple example of how to create a toggle button using Tkinter:


# import tkinter as tk

# def toggle():
#     current_state = var.get()
#     if current_state == 0:
#         label.config(text="Button is OFF")
#     else:
#         label.config(text="Button is ON")

# # Create the main window
# root = tk.Tk()
# root.title("Toggle Button Example")
# root.geometry('400x300')

# # Create a variable to store the button state
# var = tk.IntVar()

# # Create a toggle button
# toggle_button = tk.Checkbutton(root, text="Toggle", variable=var, command=toggle)
# toggle_button.pack(pady=10)

# # Create a label to display the button state
# label = tk.Label(root, text="Button is OFF")
# label.pack(pady=10)

# # Start the main loop
# root.mainloop()

# ----- In this example, we use the 'Checkbutton' widget from Tkinter and associate it with an 
# 'IntVar' variable ('var') the 'toggle' function is called whenever the button state changes.
# Depending on the state, the label text is updated to reflect whether the button is ON or OFF. -----------



# ---------------- from bard -----------------------

# A Python GUI toggle button is a special type of button that switches between two states: on and off.
# When clicked, it flips its state and updates its appearance and functionality accordingly. It's like a 
# light switch for your program, letting you control certain features or options.

# Here's a quick rundown:

#   ** Function: Toggle between two states, typically represented by text or images.

#   ** Appearance: Often displays the currently active state visually (e.g., color change, checkbox).

#   ** Uses: Control settings, enable/disable features, switch between modes, etc.

#   ** Libraries: Created using GUI libraries like Tkinter, PyQt, or Kivy.

#   Examples:

#       ** Turning of/off a dark mode theme.
#       ** Choosing between metric and imperial units.
#       ** Enabling/disabling a data processing option.
#       ** Marking checkboxes in a form..............

#       ---------------------------------- 



# ---------- let's look at the another example with codepro.lk---------------


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Toggle')
root.geometry('500x400')
root.resizable(False, False)

bulb_state = tk.BooleanVar(value=False)

def change_state():
        # print(bulb_state.get())
        if bulb_state.get():
                bulb_state.set(False)
                bulb.configure(text='OFF')
        else:
                bulb_state.set(True)
                bulb.configure(text='ON')
        print(bulb_state.get())



switch = ttk.Button(root, text='Switch', command=change_state)
switch.pack(side='bottom', pady='20')

bulb = ttk.Label(text='OFF')
bulb.place(relx=0.5, rely=0.4)


root.mainloop()

# ------ lesson 17 is over -------------








