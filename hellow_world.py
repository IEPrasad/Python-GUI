import tkinter as tk

# create a window 
root = tk.Tk()


## set a height and width 
# root.geometry('400x400')# widthxheight ## 1 method

# width, height = 400,400
# root.geometry(f'{width}x{height}') ## 2 method

width, height = 400,400 
root.geometry(f'{width}x{height}+100+100') # widthxheight+left+top

## how to stop resize
#root.resizable(True,True) ## this is the default type 
## we can change this like this 
## If we want to stop resizing we can replace 'True' with 'False' here.
#------------

## how to open the window center on the screen 
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = int(display_width/2 - width/2)
top = int(display_height/2 - height/2 )

root.geometry(f'{width}x{height}+{left}+{top}')


# create a title 
root.title('Hello World')

# add a icon 
root.iconbitmap("icon.ico")

# run the window
root.mainloop()






