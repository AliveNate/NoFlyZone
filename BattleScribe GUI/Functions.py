import tkinter as tk
from tkinter import *
from tkinter import ttk
# Adjusting PDF files
# python3 -m pip install --upgrade PyPDF3
import PyPDF2
# Work with images
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow
from PIL import Image, ImageTk
# To let us browse/open a file after button click.
from tkinter.filedialog import askopenfile
# Local functions
# Hover balloon messages
from idlelib.tooltip import Hovertip


# Simple function just as placeholder currently.
def button_clear(root):
    # Creates entry box just to have code in here. Not good for this function.
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    # Clear the text from the box
    e.delete(0, END)


def changeOnHover(button, colorOnHover, colorOnLeave):
    # function to change the properties of a button on hover over it.
    # adjust the background of the widget
    # background on entering the widget
    # bind is when the mouse enters into the widget i.e. hovers over
    button.bind("<Enter>",  func=lambda e: button.config(background=colorOnHover))
    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


def resizeButtonImage(address):
    img = Image.open(address)
    resize_image = img.resize((30, 38))
    finalimage = ImageTk.PhotoImage(resize_image)
    return finalimage


'''
# This is a convenient message box. Shows different options just keeping for future use if needed.
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x350")
def msg1():
    messagebox.showinfo('Show Information', 'Hi you got a prompt')
    messagebox.showerror('Error', 'You got an error')
    messagebox.showwarning('Warning', 'Do you accept the issue?')
    messagebox.askquestion('Ask Question', 'Do you want to continue?')
    messagebox.askokcancel('OK/Cancel', 'Are you sure?')
    messagebox.askyesno('Yes/No', 'Do you want to continue?')
    messagebox.askretrycancel('Retry', 'Failed! Do you want to try again?')

Button(root, text="Click me", command=msg1).pack(pady=50)
root.mainloop()
'''
