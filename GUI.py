import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        navbar_frame = tk.Frame(self)
        navbar_frame.pack(side=tk.TOP, fill=tk.X)

        session_recorder_button = tk.Button(navbar_frame, text="Session Recorder")
        session_recorder_button.pack(side=tk.LEFT)

        your_sessions_button = tk.Button(navbar_frame, text="Your Sessions")
        your_sessions_button.pack(side=tk.LEFT)

        current_log_button = tk.Button(navbar_frame, text="Current Log")
        current_log_button.pack(side=tk.LEFT)

        previous_session_button = tk.Button(navbar_frame, text="Previous Session")
        previous_session_button.pack(side=tk.LEFT)

        recording_frame = tk.Frame(self)
        recording_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        start_recording_button = tk.Button(recording_frame, text="Start Recording")
        start_recording_button.pack(side=tk.LEFT, padx=10, pady=10)

        stop_recording_button = tk.Button(recording_frame, text="Stop Recording")
        stop_recording_button.pack(side=tk.LEFT, padx=10, pady=10)

        log_text_box = tk.Text(recording_frame)
        log_text_box.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

if __name__ == "__main__":
    app = Application()
    app.mainloop()