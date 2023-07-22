import tkinter as tk
from tkinter import BOTTOM, messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class graph_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root


    def plot_pie(self):

        for widget in self.winfo_children():
            widget.pack_forget()

        self.load_button = tk.Button(self, text="Pie", command=self.plot_pie)
        self.load_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.load_button = tk.Button(self, text="Bar", command=self.plot_bar)
        self.load_button.pack(side=tk.LEFT, padx=10, pady=10)

        data = {key: value[0] for key, value in self.root.rf.window_times.items()}

    # the figure that will contain the plot
        fig = Figure(figsize = (10, 5),
                    dpi = 100,)

        # adding the subplot
        plot1 = fig.add_subplot(111)

        categories = list(data.keys())
        values = list(data.values())

        #plot1.bar(categories, values)
        # Creating the pie chart
        plot1.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)

        plot1.axis('equal')

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                master = self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack(side=tk.BOTTOM)

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                    self)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack(side=tk.BOTTOM)

    def plot_bar(self):

        for widget in self.winfo_children():
            widget.pack_forget()

        self.load_button = tk.Button(self, text="Pie", command=self.plot_pie)
        self.load_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.load_button = tk.Button(self, text="Bar", command=self.plot_bar)
        self.load_button.pack(side=tk.LEFT, padx=10, pady=10)

        data = {key: value[0] for key, value in self.root.rf.window_times.items()}

    # the figure that will contain the plot
        fig = Figure(figsize = (10, 5),
                    dpi = 100,)

        # adding the subplot
        plot1 = fig.add_subplot(111)

        categories = list(data.keys())
        values = list(data.values())

        plot1.bar(categories, values)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                master = self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack(side=tk.BOTTOM)

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                    self)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack(side=tk.BOTTOM)