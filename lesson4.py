
        # Python GUI- 04 |Buttons|

## we going to create a application for get sum of two numbers 
  ## let's see how to do this ...
    
## we want 
        # :: two entry fields
        # :: a button
        # :: and a label

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.title('Buttons-lesson 4')
# root.geometry('400x300')

# entry1 = ttk.Entry(root)
# entry1.pack()

# entry2 = ttk.Entry(root)
# entry2.pack()

# button = ttk.Button(root, text="Click Me")
# button.pack()

# label_1 = ttk.Label(root)
# label_1.pack()
 


# root.mainloop()

# ------- that is the main structure for that -- 
#     -------we have to do more things-------

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Buttons-lesson-4')
root.geometry('400x300')

def button_func(num1, num2):
    sum = num1+num2
    answer.set(f'Answer is{sum}')


number1 = tk.IntVar()
number2 = tk.IntVar()
answer = tk.StringVar()


entry1 = ttk.Entry(root, textvariable=number1)
entry1.pack()

entry2 = ttk.Entry(root, textvariable=number2)
entry2.pack()

button = ttk.Button(root, text="Click Me", command=lambda:button_func(number1.get(),number2.get()))
button.pack()

label_1 = ttk.Label(root, textvariable=answer)
label_1.pack()


root.mainloop()


'''
import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title('Sum Calculator')
root.geometry('400x300')

# Define the function to calculate the sum
def calculate_sum():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result.set(f'Answer is {num1 + num2}')

# Variables to store user input and the result
result = tk.StringVar()

# Create and place the input fields
entry1 = ttk.Entry(root)
entry1.pack()

entry2 = ttk.Entry(root)
entry2.pack()

# Create and place the button
button = ttk.Button(root, text="Calculate", command=calculate_sum)
button.pack()

# Create and place the label to display the result
label_result = ttk.Label(root, textvariable=result)
label_result.pack()

# Run the main loop
root.mainloop()
'''


# ------------------ lesson 4 is over -------------












