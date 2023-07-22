import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import threading
import time

import win32gui as w

import datetime
import json

class recording_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.current_window = None
        self.old_window = None

        self.start_recording_button = tk.Button(self, text="Start Recording", command=self.start_recording)
        self.start_recording_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_recording_button = tk.Button(self, text="Stop Recording", command=self.stop_recording)
        self.stop_recording_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.clear_button = tk.Button(self, text="Clear", command=self.clear)
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.save_button = tk.Button(self, text="Save Session", command=self.save_data)
        self.save_button.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.log_tree = ttk.Treeview(self, columns=('Window', 'Time', 'Active'), show='headings')
        self.log_tree.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.log_tree.heading('Time', text='Time')
        self.log_tree.heading('Window', text='Window')
        self.log_tree.heading('Active', text='Active')

        self.recording = False
        self.window_times = {}
        self.record_thread = threading.Thread(target=self.loop)

    def clear(self):
        self.recording = False
        self.log_tree.delete(*self.log_tree.get_children())
        self.window_times = {}

    def save_data(self):
        treeview_data = []
        for id in self.log_tree.get_children():
            window = self.log_tree.set(id, 'Window')
            time = self.log_tree.set(id, 'Time')
            active = self.log_tree.set(id, 'Active')
            treeview_data.append((window, time, active))

        current_datetime = datetime.datetime.now()
        # Format the date and time in a string that you want to include in the filename
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

        with open(f'./logs/{formatted_datetime}.wt', 'w') as file:
            json.dump(self.window_times, file)

        with open(f'./logs/{formatted_datetime}.ts', 'w') as file:
            json.dump(treeview_data, file)

        messagebox.showinfo("Success!", "Your logs have saved!")

    def start_recording(self):
        self.recording = True
        threading.Thread(target=self.loop).start()

    def stop_recording(self):
        self.recording = False

    def loop(self):
        while self.recording:
            self.update_current_window()
            time.sleep(1)

    def update_current_window(self):
        self.current_window = w.GetWindowText(w.GetForegroundWindow())
        # Any regex etc here

        info = self.window_times.get(self.current_window)

        if self.old_window:
            self.log_tree.set(self.old_window, 'Active', 'No')
        # if there is a new window entry
        if info == None:

            # Add the window name to the tracked list
            index = self.log_tree.insert('', 'end', values=(self.current_window, 1, 'Yes'))
            self.window_times[self.current_window] = [1, index]

            self.old_window = index

        else:
            id = info[1]
            info[0] += 1
            self.log_tree.set(id, 'Time', info[0])
            self.log_tree.set(id, 'Active', 'Yes')