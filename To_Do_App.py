import tkinter as tk
from tkinter import ttk
from datetime import datetime

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        update_progress()

def complete_task(event):
    task_index = task_listbox.curselection()
    if task_index:
        completed_task = task_listbox.get(task_index)
        history_listbox.insert(tk.END, completed_task)
        task_listbox.delete(task_index)
        update_progress()

def update_progress():
    total_tasks = task_listbox.size()
    completed_tasks = task_listbox.size() - task_listbox.size(tk.ACTIVE)
    if total_tasks > 0:
        progress = (completed_tasks / total_tasks) * 100
        progress_bar["value"] = progress

def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_clock)  # Update every 1 second

window = tk.Tk()
window.title("ToDo List")

homepage_label = tk.Label(window, text="Welcome to ToDo List!", font=("Arial", 16, "bold"))
homepage_label.pack(pady=10)

date_label = tk.Label(window, text=datetime.now().strftime("%Y-%m-%d"), font=("Arial", 12))
date_label.pack()

time_label = tk.Label(window, text=datetime.now().strftime("%H:%M:%S"), font=("Arial", 12))
time_label.pack(pady=5)

frame = tk.Frame(window)
frame.pack(pady=10)

task_listbox = tk.Listbox(frame, width=40, height=10, font=("Arial", 12))
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

entry = tk.Entry(window, width=40, font=("Arial", 12))
entry.pack()

add_task_button = tk.Button(window, text="Add Task", font=("Arial", 12), command=add_task, bd=0, padx=10, pady=5, bg="#3498db", fg="white")
add_task_button.pack(pady=5)

progress_frame = tk.Frame(window)
progress_frame.pack(pady=10)

progress_label = tk.Label(progress_frame, text="Task Completion:", font=("Arial", 12))
progress_label.pack(side=tk.LEFT)

progress_bar = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=0, mode="determinate", value=0, style="green.Horizontal.TProgressbar")
progress_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)

window.style = ttk.Style()
window.style.theme_use("default")
window.style.configure("green.Horizontal.TProgressbar", background="#2ecc71", troughcolor="white")

history_label = tk.Label(window, text="Task History:", font=("Helvetica", 14, "bold"))
history_label.pack(pady=10)

history_listbox = tk.Listbox(window, width=40, height=5, font=("Helvetica", 12))
history_listbox.pack()

task_listbox.bind("<Double-Button-1>", complete_task)

update_clock()  # Start the ticking clock

window.mainloop()
