import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import os
import json

class sessions_frame(tk.Frame):
    def __init__(self, root, recording_frame):
        super().__init__(root)
        self.root = root
        self.recording_frame = recording_frame

        self.tree = ttk.Treeview(self, columns=('File'), show='headings')
        self.tree.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree.heading('File', text='File')

        self.load_button = tk.Button(self, text="Load", command=self.load_data)
        self.load_button.pack(side=tk.LEFT, padx=10, pady=10)



    def list_files(self):
        # Get the current working directory (where the application is running)
        current_directory = os.getcwd()
        subdirectory_path = os.path.join(current_directory, 'logs')

        # Grab the files
        self.files = os.listdir(subdirectory_path)


        self.tree.delete(*self.tree.get_children())
        for entry in self.files[::2]:
            self.tree.insert('', 'end', values=[entry[:-3]])


    def load_data(self):

        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror("Error!", "You must select a log")
            return

        item_data = self.tree.item(selected_item)['values'][0]

        with open(f'./logs/{item_data}.wt', 'r') as file:
            self.recording_frame.window_times = json.load(file)

        with open(f'./logs/{item_data}.ts', 'r') as file:
            treeview_data = json.load(file)

        # reset old stuff!
        self.recording_frame.log_tree.delete(*self.recording_frame.log_tree.get_children())
        for window, time, active in treeview_data:
            self.recording_frame.log_tree.insert('', 'end', values=(window, time, active))

        self.root.load_recording()