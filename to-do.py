# python GUI projects
#     create a to-do APP using tkinter

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

END = True
app = tk.Tk()
app.title("to do list")
app.geometry("350x350")
ctk.set_appearance_mode("dark")

font_1 = ("Arial", 30, "bold")
font_2 = ("Arial", 18, "bold")
font_3 = ("Arial", 10, "bold")

def add_task():
    task = prompt.get()
    if task:
        task_list.insert(0, task)
        prompt.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror("Error", "Enter a task")

def remove_tasks():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected[0])
        save_tasks() 
    else:
        messagebox.showerror("Error", "Choose a task to delete") 
        
def save_tasks():
    with open("credentials.txt", "w") as f:
        tasks = task_list.get(0, END)
        for task in tasks:
            f.write(task + "\n")          

def load_tasks():
    try:
        with open("credentials.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                task_list.insert(0, task.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "Cannot load task")
        
def on_closing():
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
        app.destroy()
             
                    
title_label = ctk.CTkLabel(master=app, font=font_1, height=512, width=512)
title_label.place(x=10, y=110)

prompt = ctk.CTkEntry(master=app, font=font_2, width=330, height=28, corner_radius=2, text_color="black", fg_color="white")
prompt.place(x=10, y=10)

add_button = ctk.CTkButton(master=app, font=font_2, height=40, width=80, text_color="white", fg_color="blue", command=add_task, text="add task", hover_color="light blue")
add_button.place(x=20, y=60)

remove_button = ctk.CTkButton(master=app, font=font_2, height=40, width=80, text_color="white", fg_color="blue", command=remove_tasks, text="remove task")
remove_button.place(x=206, y=60)

task_list = tk.Listbox(master=app, width=39, height=15, font=font_3, background="grey")
task_list.place(x=40, y=120)

app.protocol("WM_DELETE_WINDOW", on_closing)

load_tasks()
app.mainloop()
