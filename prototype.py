from pywinauto import Application

app = Application(backend='uia')
app.connect(title_re=".*Chrome.*")
element_name="Address and search bar"
dlg = app.top_window()

from tkinter import *

Main_window = Tk()

def update_tab():

    url = dlg.child_window(title=element_name, control_type="Edit").get_value()

    my_label.config(text = f"tab: {url}")


my_button = Button(Main_window,
                   text = "Update tab",
                   command = update_tab)

my_label = Label(Main_window,
                 text = "Tab: ")

my_label.pack()
my_button.pack()

Main_window.mainloop()