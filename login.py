import tkinter as tk
from tkinter import messagebox as mb

class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.username = tk.Label(self, text="Username", font=("Ariel", 16))
        self.password = tk.Label(self, text="Password", font=("Ariel", 16))

        self.username_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="#")

        self.username.grid(row=0, sticky=tk.E)
        self.password.grid(row=1, sticky=tk.E)
        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        self.button = tk.Button(self, text="Login", command=self.login)
        self.button.grid(columnspan=2)

        self.pack()

    def login(self):
        get_username = self.username_entry.get()
        get_password = self.password_entry.get()
        if get_username == "User_name" and get_password == "Pass_word":
            mb.showinfo("Login", "login successful")
        else:
            mb.showerror("Login", "login failed")

    def on_closing(self):
        mb.askyesno(title="Quit", message="Are you sure you want to quit?")
        self.master.destroy()

app = tk.Tk()
login = Login(app)
app.protocol("WM_DELETE_WINDOW", login.on_closing)
app.mainloop()

