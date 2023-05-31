"""create a text editor GUI with Python that can create, open, edit, and save text files. We need three important widgets to create the desired text editor GUI with Python; 2 button widgets to save and close, and a text box widget to create and edit text files.
All the widgets should be arranged in a manner so that the buttons widgets are on the left side of the window layout and the text box widget is on the right side.
The entire window must have a minimum height of 800 pixels and the text box widget must have a minimum width of 800 pixels. The whole layout should be responsive so that if the window is resized, the text box widget is also resized

use the Tkinter package in Python to build a text editor GUI with Python. So now that we are ready with the idea let’s get started with the code.

I will simply start with importing the Tkinter package and by defining the variables with respective widgets that I discussed above. If you are using the Tkinter package for the first time you don’t need to install this using any pip command, as this comes preinstalled in the Python Virtual environment. Now let’s get started with the code to create a Text Editor GUI with Python:"""

import tkinter as tk
window = tk.Tk()
window.title("Thecleverprogrammer")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text='Open')
btn_save = tk.Button(fr_buttons, text="Save As")

#Now, let’s work on the layout of our text editor. First, we need to assign the buttons to the frame:

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

#Since we’ve assigned the buttons to the frame of our text editor, we now need to set up a grid layout for our main window:

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

#Now, if you will run the code by using the window.mainloop() function the layout of our text editor GUI will be displayed:

"""But this is just a layout, it won’t do any task at this point. Now we need to create two functions so that we can write, save and edit using this text editor GUI.

Function to Open file:"""

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Thecleverprogrammer - {filepath}")
    
 
#Function to save file:

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Thecleverprogrammer - {filepath}")
    
    
#our full code will look like:

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Thecleverprogrammer - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Thecleverprogrammer - {filepath}")

window = tk.Tk()
window.title("Thecleverprogrammer")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
