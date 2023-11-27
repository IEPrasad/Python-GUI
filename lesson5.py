

            # Python GUI - 05 | Checkbox |

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title('Checkbox')
# root.geometry('300x200')
# root.resizable(False, False)

# label_var = tk.StringVar()
# check1_var = tk.StringVar()
# check2_var = tk.StringVar()

# def checkbox_results():
#     output_string = "Selected languages: " + check1_var.get() + " " + check2_var.get()
#     label_var.set(output_string)
#     # print(check1_var.get())
#     # print(check2_var.get())


# check1 = ttk.Checkbutton(root, text="Python",variable=check1_var, onvalue='Python', offvalue='')
# check1.pack()

# check2 = ttk.Checkbutton(root, text="Java", variable=check2_var, onvalue='Java', offvalue='')
# check2.pack()

# button = ttk.Button(root, text='Click Me', command=checkbox_results)
# button.pack()

# label = ttk.Label(root, textvariable=label_var)
# label.pack()

# root.mainloop()

# continue with 11 minute --------


### we can put these two variable in a list like this ---------->>>
        #    (  check1_var = tk.StringVar()
            # check2_var = tk.StringVar() )


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Checkbox')
root.geometry('300x200')
root.resizable(False, False)

label_var = tk.StringVar()
checkbox_values = [tk.StringVar(), tk.StringVar()]

def checkbox_results():
    output_string = "Selected languages: " + checkbox_values[0].get() + " " + checkbox_values[1].get()
    label_var.set(output_string)
    # print(check1_var.get())
    # print(check2_var.get())


check1 = ttk.Checkbutton(root, text="Python",variable=checkbox_values[0], onvalue='Python', offvalue='')
check1.pack()

check2 = ttk.Checkbutton(root, text="Java", variable=checkbox_values[1], onvalue='Java', offvalue='')
check2.pack()

button = ttk.Button(root, text='Click Me', command=checkbox_results)
button.pack()

label = ttk.Label(root, textvariable=label_var)
label.pack()

root.mainloop()



# ------ lesson 5 is over ----------------------    
