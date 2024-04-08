# python GUI projects
#     basic clock GUI using tkinter

# import all libraries and dependencies
import tkinter as tk
import customtkinter as ctk
from datetime import datetime
from time import strftime

# set the GUI application
root = tk.Tk()
root.geometry("400x250")
root.title("clock")
ctk.set_appearance_mode("dark")

# set the clock font and style
Label = tk.Label(root, font=("Helvetica",
                             60), background="gray", foreground="black")
Label.pack(anchor="center")


def update_time():
    current_time = strftime("%H:%M:%S")
    Label.config(text=current_time)
    Label.after(1000, update_time)


# define the time function
def time():
    string = strftime("%H:%M:%S")
    Label.config(text=string)
    Label.after(1000, update_time)


# define the stop watch function
class StopWatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.is_running = False
        self.start_time = None
        self.total_elapsed_time = 0

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        self.label = tk.Label(root, textvariable=self.time_var, font=("Helvetica", 24))
        self.label.pack(pady=10)

        self.start_button = ctk.CTkButton(root, text="Start", command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = ctk.CTkButton(root, text="Reset", command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.RIGHT, padx=5)

        self.update_display()

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.root.after(100, self.update_stopwatch)
            self.start_button.configure(text="Stop")
        else:
            self.is_running = False
            self.total_elapsed_time += (datetime.now() - self.start_time).total_seconds()  # type: ignore
            self.start_button.configure(text="Start")

    def reset_stopwatch(self):
        self.is_running = False
        self.start_time = None
        self.total_elapsed_time = 0
        self.time_var.set("00:00:00")
        self.start_button.configure(text="Start")

    def update_stopwatch(self):
        if self.is_running:
            elapsed_time = self.total_elapsed_time + (datetime.now() - self.start_time).total_seconds()
            elapsed_time_str = self.format_time(elapsed_time)
            self.time_var.set(elapsed_time_str)
            self.root.after(100, self.update_stopwatch)

    def update_display(self):
        if self.is_running:
            self.update_stopwatch()

    def format_time(self, elapsed_time):
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"


def stop_watch():
    stop_watch_window = tk.Toplevel(root)
    stop_watch_obj = StopWatch(stop_watch_window)
    stop_watch_obj.format_time


# clock butons using custom tkinter
trigger = ctk.CTkButton(master=root, height=40, width=120, corner_radius=30, text_color="white", command=stop_watch)
trigger.configure(text="stop watch")
trigger.place(x=140, y=150)

# call time and run mainloop
time()
root.mainloop()
