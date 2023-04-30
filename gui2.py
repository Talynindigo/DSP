import tkinter as tk

# Create a tkinter window
window = tk.Tk()

# Set the window title
window.title("Activity Logger")

# Set the window size
window.geometry("800x600")

# Create the navbar frame
navbar_frame = tk.Frame(window, bg="#333")

# Create the navbar buttons
session_recorder_btn = tk.Button(navbar_frame, text="Session Recorder", fg="white", bg="#333", padx=10)
your_sessions_btn = tk.Button(navbar_frame, text="Your Sessions", fg="white", bg="#333", padx=10)
current_log_btn = tk.Button(navbar_frame, text="Current Log", fg="white", bg="#333", padx=10)
previous_session_btn = tk.Button(navbar_frame, text="Previous Session", fg="white", bg="#333", padx=10)

# Pack the navbar buttons
session_recorder_btn.pack(side="left")
your_sessions_btn.pack(side="left")
current_log_btn.pack(side="left")
previous_session_btn.pack(side="left")

# Create the logs frame
logs_frame = tk.Frame(window, bg="white")

# Create the log buttons
log1_btn = tk.Button(logs_frame, text="Log 1", padx=10)
log2_btn = tk.Button(logs_frame, text="Log 2", padx=10)
log3_btn = tk.Button(logs_frame, text="Log 3", padx=10)
log4_btn = tk.Button(logs_frame, text="Log 4", padx=10)

# Pack the log buttons
log1_btn.pack(side="left", padx=10)
log2_btn.pack(side="left", padx=10)
log3_btn.pack(side="left", padx=10)
log4_btn.pack(side="left", padx=10)

# Create the text box frame
text_box_frame = tk.Frame(window)

# Create the text box label
text_box_label = tk.Label(text_box_frame, text="Text Box", font=("Helvetica", 14))

# Create the text box
text_box = tk.Text(text_box_frame)

# Pack the text box label and text box
text_box_label.pack(pady=10)
text_box.pack()

# Pack the navbar frame, logs frame, and text box frame
navbar_frame.pack(fill="x")
logs_frame.pack(fill="x", pady=10)
text_box_frame.pack(fill="both", expand=True)

# Run the tkinter event loop
window.mainloop()
