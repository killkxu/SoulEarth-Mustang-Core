# gui_memory_panel.py
import tkinter as tk
from memory_logger import memory_logger

def launch_gui_panel():
    window = tk.Tk()
    window.title("SoulEarth GUI Memory Panel")

    label = tk.Label(window, text="🧠 Welcome to the SoulEarth Memory Panel", font=("Arial", 14), pady=10)
    label.pack()

    log_button = tk.Button(window, text="Log Memory Event", command=lambda: memory_logger.log_event("Manual GUI Memory Event Logged."))
    log_button.pack(pady=10)

    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.pack(pady=10)

    memory_logger.log_event("🧠 GUI Memory Panel Launched.")
    window.mainloop()
