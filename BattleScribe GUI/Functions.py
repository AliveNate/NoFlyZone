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


def dropDownOneSection(root, oldBtn, btnLstAry, position):
    # Button lists = [arrayPosition, name, symbol, xbutton, xLabel, yPosition]
    # Create a list with button attributes, and append to array
    # Button list for this button was just appended to the array of lists
    # Grab last list from the array and get the attributes
    # Use these to help create the new button/label
    oldBtnPos = btnLstAry[-1][0]
    # Get the old
    oldBtnName = btnLstAry[-1][1]
    # Need to send in the button as an object to change the label here.
    oldBtn["text"] = "-"
    oldBtn["command"] = lambda: pullUpOneSection(root, oldBtn, btnLstAry, position+1)
    oldBtnSym = btnLstAry[-1][2]
    oldbtnX = btnLstAry[-1][3]
    oldlblX = btnLstAry[-1][4]
    oldYPlace = btnLstAry[-1][5]
    # When a user clicks the + button, it drops down a new +button, label, and turns this button into a -

    # The expanded next level button
    newYPlace = oldYPlace + 41
    # Grab text from original button name and add a position for the new button name
    newBtnName = oldBtnName + str(oldBtnPos+1)
    # Create list with the new buttons attributes.
    newBtnLst = [(oldBtnPos + 1), newBtnName, "+", oldbtnX, oldlblX, newYPlace]
    # Append the list to the original array of lists.
    btnLstAry.append(newBtnLst)
    # Create the new button, and these attributes have been added to the new list, and the list was appended to the array
    newBtn = Button(root, text="+", command=lambda: dropDownOneSection(root, newBtn, btnLstAry, position), relief=FLAT, background="gray")
    newBtn.place(x=oldbtnX, y=newYPlace, height=40, width=20)
    newlabel1 = Label(root, text=newBtnName, borderwidth=1, relief="solid")
    newlabel1.place(x=oldlblX, y=newYPlace, height=40, width=200)


def pullUpOneSection(root, oldBtnName, btnLstAry, position):
    i = 0
    pos = 0
    oldBtnName["text"] = "xxx"
    # destroyx





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
