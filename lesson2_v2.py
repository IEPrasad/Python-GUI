
    # Python GUI-02 |Basic Widgets|

                ## We are going to learn here about 3 widgets 
                        ## enrtry fields 
                        ## button
                        ## label

import tkinter as tk
from tkinter import ttk


root = tk.Tk()

root.title("Basic Widgets")
root.geometry('300x200')
# root.resizable(False,False)

# create a function regarding 5
# def button_click_func():
#     print('Helloooo')
## now we have to change this function 

def button_click_func():
    entry_field_value = entry.get()
    # print(entry_field_value)  # we have to check that like this
    label.configure(text=entry_field_value) ## $$ from this we have to do our job
    ## or without creating variable we have to put this like this
    # label.configure(text=entry.get()) ## this is for the without entry_filed_value function

    button_2.configure(state="disabled")## regarding 6



# 1- let's create a button -type 1
button_1 = tk.Button(root, text="Click Me-type1")
button_1.pack()

# 3- let's create a entry field above in button_2
entry = ttk.Entry(root)
entry.pack()

# 2- let's create a button with ttk library
# button_2 = ttk.Button(root, text="Click Me-type2")
# button_2.pack()

# considering 5--->>
# button_2 = ttk.Button(root, text="Click Me-type2", command= button_click_func())
## don't put the brackets 
button_2 = ttk.Button(root, text="Click Me-type2", command= button_click_func)
button_2.pack()


# 4- now we want to do these entry field value set as a label after entred value
# and after we click the button we have to show the entry filed value in a label
        # firstly see how to create a label 
            #   label = ttk.Label(root)
                # label.pack()
                # but now we can't see the label 
                # if we want to see our label 
                # label.configure(text="Hello")

# label = ttk.Label(root)
# label.pack()
# label.configure(text="Hello this is the label   ")


# 5- now we have to create a function regardin the click button 
label = ttk.Label(root)
label.pack()

# 6- now we have to set after click the button it going to disable


root.mainloop()





            # ----------- lesson 2 is over and -----------keep learning----------






















