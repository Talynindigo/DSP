import tkinter as tk
from tkinter import ttk

import threading
import time

import win32gui as w
from graphs import graph_frame
from past_sessions import sessions_frame

from recording import recording_frame

class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        # Components
        navbar_frame = tk.Frame(self)
        navbar_frame.pack(side=tk.TOP, fill=tk.X)

        session_recorder_button = tk.Button(
            navbar_frame,
            text="Session Recorder",
            command=self.load_recording
        )

        session_recorder_button.pack(side=tk.LEFT)

        your_sessions_button = tk.Button(
            navbar_frame,
            text="Your Sessions",
            command=self.load_sessions
        )

        your_sessions_button.pack(side=tk.LEFT)

        graph_button = tk.Button(
            navbar_frame,
            text="Graph",
            command=self.load_graph
        )

        graph_button.pack(side=tk.LEFT)

        self.rf = recording_frame(self)
        self.sf = sessions_frame(self, self.rf)
        self.gf = graph_frame(self)

        self.rf.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def load_recording(self):
        self.sf.pack_forget()
        self.gf.pack_forget()

        self.rf.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def load_sessions(self):
        self.rf.pack_forget()
        self.gf.pack_forget()
        self.rf.recording = False

        self.sf.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.sf.list_files()

    def load_graph(self):
        self.rf.pack_forget()
        self.sf.pack_forget()

        self.gf.plot_pie()
        self.gf.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = Application()
    app.mainloop()