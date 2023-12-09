              

                    # Python GUI - 11 | Canvas | 
'''
            ** The Python GUI Canva is a graphical widget that serves as a drawing area
            within graphical user interface (GUI) frameworks such as Tkinter. It provides a 
            versatile space for creating and displaying graphics, shapes, images, and 
            other visual elements. Developers can use the Canvas widged to implement
            custom drawings, animations, and interactive visual components in their GUI
            applications. The Canvas supports various methods for drawing shapes, lines,
            text, and images, making it a powerful tool for building dynamic and visually 
            appealing interfaces.....  '''


# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title("Canvas")
# root.geometry('500x400')
# root.resizable(False, False)

# canvas = tk.Canvas(root, bg='white')
# canvas.pack()

# canvas.create_rectangle((10, 20, 60, 170), fill='gray')
# canvas.create_oval((110, 9, 200, 150), fill='green')
# canvas.create_polygon((255, 200, 255, 30, 200, 270), fill='red')

# # canvas.create_line((0, 0, 300, 255))
# canvas.create_line((0, 0, 300, 255), fill='blue', width=5)

# root.mainloop()

# ----------------------------

# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# root.title('Events')
# root.geometry('500x400')
# root.resizable(False, False)

# canvas = tk.Canvas(root, bg='white')
# canvas.pack()

# # canvas.bind('Motion', lambda event:print(event))

# brush_width = 5

# def draw(event):
#   x = event.x
#   y = event.y
#   # canvas.create_oval((x, y, x, y))
#   # canvas.create_oval((x-1, y-1, x+1, y+1))
#   # canvas.create_oval((x-15, y-15, x+12, y+13))

#   #we can add a variable for that 
#   canvas.create_oval((x-brush_width, y-brush_width, x+brush_width, y+brush_width))
  

# canvas.bind('<Motion>', draw )

# root.mainloop()

### now these code has a little bit problem 
# when we moving the mouse these circles are displayin on the 
# canvas 
# now we want to develop our code for when we click and moving
# the mouse so then the circles are creating on the canvas
## now let's see how to do this 

# ===---------------->>>

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Events')
root.geometry('500x400')
root.resizable(False, False)

canvas = tk.Canvas(root, bg='white')
canvas.pack()

brush_width = 3

def draw(event):
  x = event.x
  y = event.y
  canvas.create_oval((x-brush_width, y-brush_width, x+brush_width, y+brush_width), fill='Black')

def start_drawing(event):
  x = event.x
  y = event.y
  # canvas.create_oval((x-brush_width, y-brush_width, x+brush_width, y+brush_width))
  canvas.create_oval((x-brush_width, y-brush_width, x+brush_width, y+brush_width), fill='black')
  canvas.bind('<B1-Motion>', draw)


canvas.bind('<Button-1>', start_drawing)


root.mainloop()



# ------------ lesson 11 is over but canvas is not over ----------------

# practice more-------------












