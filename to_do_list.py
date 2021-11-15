import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("to do list")

def add_task():
    task = entry_task.get()
    if task!=:
        Listbox_tasks.insert(tkinter.END ,task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning", message="You must enter a task.")

def delete_task():
    try:
        task_index = Listbox_tasks.curselection()[0]
        Listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning" , message="You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("task.dat" , "rb"))
        Listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            Listbox_tasks.insert(tkinter.END, task)
    except:
            tkinter.messagebox.showwarning(title="warning" , message="Cannot finf tasks.dat")

def save_task():
    tasks = Listbox_tasks.get(0, Listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat" , "wb")) 


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

button_add_task= tkinter.Button(root, text="Add task",width=48, command = add_task)
button_add_task.pack()

button_delete_task= tkinter.Button(root, text="Delete task",width=48, command = delete_task)
button_delete_task.pack()

button_load_tasks= tkinter.Button(root, text="Load tasks",width=48, command = load_tasks)
button_load_tasks.pack()

button_save_task= tkinter.Button(root, text="Save task",width=48, command = save_task)
button_save_task.pack() 

root.mainloop()