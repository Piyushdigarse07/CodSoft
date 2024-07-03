from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("To-Do List")

# Function to add a task to the list
def enter():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(END, task)
        entry_task.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")
#Function to delete task
def deletetask():
    try:
        selected_task_index = listbox_task.curselection()[0]
        listbox_task.delete(selected_task_index)
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task to delete.")

# Function to mark a task as completed
def completed():
    try:
        selected_task_index = listbox_task.curselection()[0]
        task = listbox_task.get(selected_task_index)
        listbox_task.delete(selected_task_index)
        listbox_task.insert(END, task + " ✔")
        tkinter.messagebox.showwarning(title="Honour"+" ✔",message="Well Done! for completing the task.")
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task to mark as done.")

frame_task = Frame(window)
frame_task.pack()

# Listbox for tasks
listbox_task = Listbox(frame_task, bg="pink", fg="black", height=15, width=50, font="Helvetica")
listbox_task.pack(side=LEFT)

# Box for input tasks
entry_task = Entry(window, width=50)
entry_task.pack(pady=3)

# Buttons to add, delete, and mark tasks as completed
entry_button = Button(window, text="Add task", width=50, command=enter)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as Done", width=50, command=completed)
mark_button.pack(pady=3)

window.mainloop()
