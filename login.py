import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        
        self.menu_bar = tk.Menu(self.root)
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close Without Question", command=exit)
        
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")
        self.root.config(menu=self.menu_bar)
        
        self.label = tk.Label(self.root, text="hello world", font=("Arial", 10))
        self.label.pack(padx=20, pady=20)
        
        self.text_box = tk.Text(self.root, height=3, font=("Arial", 16))
        self.text_box.bind("<KeyPress>", self.shortcut)
        self.text_box.pack(padx=10)
        
        self.check_state = tk.IntVar()
        
        self.check= tk.Checkbutton(self.root, text="show message", font=("Arial", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="show message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        self.clear_button = tk.Button(self.root, text="clear", font=("Arial", 16), command=self.clear)
        self.clear_button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.text_box.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="message", message=self.text_box.get("1.0", tk.END))
            
    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
            
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
            
    def clear(self):
        self.text_box.delete("1.0", tk.END)
        
            
MyGUI()