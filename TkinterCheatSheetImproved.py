#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *

# Initialize the main window with title and size
def initialize_window():
    window = Tk()
    window.title("Responsive GUI Layout")
    window.minsize(400, 300)  # Adjusted minimum size for better layout
    return window

top = initialize_window()

# --- Scale Widget Callback ---
def scale_callback(value):
    L.configure(text=f"The Angle is: {value}°")

# --- Button Widget Callback ---
def button_callback():
    L.configure(text="The button was Clicked !!")

# --- Entry Widget Callback ---
def entry_callback():
    L.configure(text=E.get())

# --- Checkbox Widget Callback ---
def checkbox_callback():
    # Check the status of all checkboxes and update the label accordingly
    selected_options = []
    if CbVar1.get():
        selected_options.append("Option 1")
    if CbVar2.get():
        selected_options.append("Option 2")
    if CbVar3.get():
        selected_options.append("Option 3")
    
    # If no options selected
    if not selected_options:
        L.configure(text="No options selected")
    else:
        L.configure(text="Selected: " + ", ".join(selected_options))

# --- Layout Creation with Frames ---

# Configure grid weights to allow resizing
top.grid_rowconfigure(0, weight=1)  # Make the first row (label row) expand
top.grid_rowconfigure(1, weight=2)  # Control frame row should expand more
top.grid_rowconfigure(2, weight=1)  # Exit button at the bottom
top.grid_columnconfigure(0, weight=1)  # Make the single column expand

# 1. Display Label at the Top (centered and large)
L = Label(top, text="Hello!", font=("Arial", 16, "bold"))
L.grid(row=0, column=0, padx=10, pady=20, sticky="n")  # Placed at the top center, sticky north

# Main Frame for all controls (Scale, Entry, Checkbox, Buttons)
control_frame = Frame(top)
control_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Expands and fills the middle part

# Configure grid weights inside the control frame to allow for dynamic resizing
control_frame.grid_rowconfigure(0, weight=1)
control_frame.grid_rowconfigure(1, weight=1)
control_frame.grid_rowconfigure(2, weight=1)
control_frame.grid_columnconfigure(0, weight=1)

# 2. Scale Section
scale_frame = Frame(control_frame)
scale_frame.grid(row=0, column=0, pady=10, sticky="ew")  # Make it fill horizontally
Label(scale_frame, text="Angle:", font=("Arial", 12)).pack(side=LEFT, padx=(0, 10))
Scale(scale_frame, command=scale_callback, from_=10, to=180, orient=HORIZONTAL).pack(side=LEFT, fill=X, expand=True)

# 3. Entry Section
entry_frame = Frame(control_frame)
entry_frame.grid(row=1, column=0, pady=10, sticky="ew")
Label(entry_frame, text="Input:", font=("Arial", 12)).pack(side=LEFT, padx=(0, 10))
E = Entry(entry_frame, bd=2, width=25)
E.pack(side=LEFT, fill=X, expand=True)
E.focus_set()  # Focus on entry field when the window loads
Button(entry_frame, text="Submit", command=entry_callback).pack(side=LEFT, padx=10)

# 4. Checkbox Section
checkbox_frame = Frame(control_frame)
checkbox_frame.grid(row=2, column=0, pady=10, sticky="ew")

# Variables to store the state of the checkboxes
CbVar1 = IntVar()
CbVar2 = IntVar()
CbVar3 = IntVar()

# Three checkboxes for Option 1, Option 2, and Option 3
Checkbutton(checkbox_frame, text="Option 1", variable=CbVar1, font=("Arial", 12)).pack(side=LEFT)
Checkbutton(checkbox_frame, text="Option 2", variable=CbVar2, font=("Arial", 12)).pack(side=LEFT, padx=10)
Checkbutton(checkbox_frame, text="Option 3", variable=CbVar3, font=("Arial", 12)).pack(side=LEFT)

# Button to check the state of all checkboxes
Button(checkbox_frame, text="Check", command=checkbox_callback).pack(side=LEFT, padx=10)

# 5. Exit Button at the Bottom
Button(top, text="Exit", command=top.quit).grid(row=2, column=0, pady=10, sticky="s")  # Bottom center, sticky south

# Start the Tkinter event loop
top.mainloop()
