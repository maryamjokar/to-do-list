import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("to do list")

#create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

Listbox_tasks=tkinter.Listbox(root,height=3, width=50)
Listbox_tasks.pack(side=tkinter.LEFT)


root.mainloop()