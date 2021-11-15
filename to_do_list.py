import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("to do list")

#create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

Listbox_tasks=tkinter.Listbox(root,height=3, width=50)
Listbox_tasks.pack(side=tkinter.LEFT)

Scrollbar_task = tkinter.Scrollbar(frame_tasks)
Scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

Listbox_tasks.config(yscrollcommand=Scrollbar_task.set)
Scrollbar_task.config(command=Listbox_tasks.yview)

entry_task= tkinter.Entry(root,width=50)
entry_task.pack()


root.mainloop()