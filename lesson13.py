
            # Python GUI - 13 |Frames|
'''
     ** In Python GUI programming, a Frame is a container widget that serves as a grouping 
     mechanism for organizing and structuring other GUI elements. Frames are used to group 
     related widgets together, creating a logical separation within a graphical user interface 
     (GUI). They help in organzing the layout and structure of a GUI application by providing a 
     way to group and manage other widgets, such as buttons, labels, or input fields, within a 
     common area. Frames are particularly useful for modularizing the GUI and enhancing code 
     oraganization, making it easier to manage and maintain complex user interfaces......
                                                                                          '''

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('Frames')
# root.geometry('500x400')
 
# frame1 = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
# # frame1.pack()
# ## we can change the alignment like these, 
# # top, right, left, bottom
# frame1.pack(side='bottom')


# root.mainloop()


# ----------- now let's see how to add a entry field 
# for these frame -----------


'''
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('500x400')
root.title('Frames')

frame2 = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame2.pack(side='left')

# kalin api laba dunne master eka sadaha
# root we. namuth api dan laba denne adala frame eke nama we
entry = ttk.Entry(frame2) 
frame2.pack_propagate(False)
entry.pack(pady=10)

## but now when we add a entry or another thing we have lost over
# main border, because it is resize automatically...
## we can use the propagate(True) >> False---for fix these problem 

# add a padding we can use pady = 10 
# or padx = 20

root.mainloop()

'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Frames')
root.geometry('500x400')

frame3 = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame3.pack_propagate(False)
frame3.pack(side='left')

entry = ttk.Entry(frame3)
entry.pack(pady=10)

button = ttk.Button(frame3, text='Submit')
button.pack()

frame4 = ttk.Frame(root, width=200, height=100, relief=tk.GROOVE)
frame4.pack_propagate(False)
frame4.pack(pady=30)

label = ttk.Label(frame4, text='Welcome')
label.pack(pady=10)

button2 = ttk.Button(frame4, text='Click Me')
button2.pack(pady=10)


root.mainloop()


# ------------- 13 is over ------------------ 














