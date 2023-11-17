

		# |Python GUI - tutorial | lesson-1 |

'''

	** Tkinter is the standard GUI (Graphical User Interface) toolkit for Python.
		It provides a set of tools to create windows, dialoags, buttons, textboxes,
		and, other GUI elements for your Python applications. Tkinter is easy to learn 
		and use, making it a popular choice for beginners in GUI programming...


		--- Here's a brief overview of some key components in Tkinter: '

		1- Widgets: 
				Tkinter provides a variety of widgets such as buttons, lables, entry
				fields, textboxes, and more. These are the building blocks for 
				constructing your GUI.

		2- Geometry Managers:
				Tkinter uses geometry managers (like 'pack()', 'gird()', and 'place()')
				to oraganize and arrange widgets within the window.

		3- Event Handling: 
				Tkinter allows you to bind functions (event handlers) to events,
				such as button click or key presses, enabling your applications to 
				respond to user interfaces.

		4- Main Event Loop: 
				Tkinter operators on an event-driven programming model. The main event 
				loop ('mainlooop()') continuously listens for events (e.g., button
				clicks) and triggers the corresponding event handlers.

				Here's a simple template to create a basic Tkinter window:'


				import tkinter as tk

				# Create the main window
				root = tk.TK()

				# Add widgets and set up the GUI 

				# Start the Tkinter event loop 
				root.mainloop()




		You can build upon this template by adding widgets, defining their properties,
		and incorporating event handling to create interactive applications.

				------------------------------------------ '''


# >>>---->> 

	## we can download .ico file and then we can use to that image for the icon 

#--------- Instructions for the hellow_world.py file 

# First we have to import tkinter as tk
# create a window 
	# root = tk.Tk()

# run the window 	
	# root.mainloop()
# create a title 
	# root.title('Hello World')

# add a icon
	# root.iconbitmap('icon.ico')

# set height and width
	# root.geometry(400x400) # widthxheight
		## we have to put this line after the create a window line
	# and also we have to create that like this if we want 	
		# height, width = 400, 400
		# root.geometry(f'{width}x{height}')

## this is is startin left up corner, (0,0 point)
#   we have to change this 
		# root.geometry(f'{width}x{height}+100+100') # widthxheight + left + top


## how to stop resize
#root.resizable(True,True) ## this is the default type 
## we can change this like this 
## If we want to stop resizing we can replace 'True' with 'False' here.

## now let's see how to open this window center on the screen

## we can get screen width and height using Python 
## and we have to create a formula for doing that 
## --->>
## Screen width/2 - width/2 , Screen height/2 - height/2


## the mainloop is always running. after close the window it will stop, then
## another lines will be executed


















