
      # Python GUI -15 | Menu |

import tkinter as tk


root = tk.Tk()
root.title('Menu')
root.geometry('500x400')

menu = tk.Menu(root)

light_result = tk.StringVar(value='OFF')

file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda:print('New'))
file_menu.add_command(label='Open', command=lambda:print('Open'))
menu.add_cascade(label='File', menu=file_menu)

result_menu = tk.Menu(menu, tearoff=False)
result_menu.add_command(label='Display')
result_menu.add_checkbutton(label='Light', variable=light_result, onvalue='ON', offvalue='OFF', command=lambda:print(light_result.get()))
menu.add_cascade(label='Options', menu=result_menu)

root.configure(menu=menu)


root.mainloop()