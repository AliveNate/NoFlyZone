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
from Functions import *


root = tk.Tk()
root.title("BattleScribe")
root.geometry("600x600")
# This form needs a png image. This image is in the same directory currently.
root.iconphoto(False, tk.PhotoImage(file="battlescribeLogo.png"))


# Sets up grid so that we can use the NSEW stretch params
root.rowconfigure(0, weight=2)
root.columnconfigure(0, weight=1)


# Simple function just as placeholder currently.
def button_clear():
    # Creates entry box just to have code in here. Not good for this function.
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    # Clear the text from the box
    e.delete(0, END)


# Use  lambda to pass a var/value to a button function (command=lambda: button_click(1)))
button_NoFlyZone            = Button(root, text="NoFlyZone.com", padx=10, pady=10, command=button_clear)
button_CreateNewRoster      = Button(root, text="1", padx=12, pady=10, command=button_clear)
button_OpenExistingRoster   = Button(root, text="2", padx=12, pady=10, command=button_clear)
button_OpenRosterToView     = Button(root, text="3", padx=12, pady=10, command=button_clear)
button_SaveTheRoster        = Button(root, text="4", padx=11, pady=10, command=button_clear)
button_SaveTheRosterAs      = Button(root, text="5", padx=11, pady=10, command=button_clear)
button_ViewTheRoster        = Button(root, text="6", padx=11, pady=10, command=button_clear)
button_ShareTheRoster       = Button(root, text="7", padx=11, pady=10, command=button_clear)
button_PrintTheRoster       = Button(root, text="8", padx=11, pady=10, command=button_clear)
button_ManageData           = Button(root, text="9", padx=11, pady=10, command=button_clear)
button_SupportBattleScribe  = Button(root, text="10", padx=11, pady=10, command=button_clear)
button_DiceTool             = Button(root, text="11", padx=11, pady=10, command=button_clear)
button_Updates              = Button(root, text="12", padx=10, pady=10, command=button_clear)
button_ReportABug           = Button(root, text="13", padx=10, pady=10, command=button_clear)

# Put buttons on the screen
# sticky="NSEW"  Lets us stretch items if the window gets bigger in real time.
button_NoFlyZone.grid(          row=0, column=0, sticky="NEW")
button_CreateNewRoster.grid(    row=0, column=1, sticky="NE")
button_OpenExistingRoster.grid( row=0, column=2, sticky="NE")
button_OpenRosterToView.grid(   row=0, column=3, sticky="NE")
button_SaveTheRoster.grid(      row=0, column=4, sticky="NE")
button_SaveTheRosterAs.grid(    row=0, column=5, sticky="NE")
button_ViewTheRoster.grid(      row=0, column=6, sticky="NE")
button_ShareTheRoster.grid(     row=0, column=7, sticky="NE")
button_PrintTheRoster.grid(     row=0, column=8, sticky="NE")
button_ManageData.grid(         row=0, column=9, sticky="NE")
button_SupportBattleScribe.grid(row=0, column=10, sticky="NE")
button_DiceTool.grid(           row=0, column=11, sticky="NE")
button_Updates.grid(            row=0, column=12, sticky="NE")
button_ReportABug.grid(         row=0, column=13, sticky="NEW")

#paddinglabel = StringVar()
#label = Label(root, textvariable=paddinglabel, relief=RAISED)
#paddinglabel.set("NoFlyZone.com")
#label.grid(row=0, column=13, sticky=NE)

# Spacing line to show separator after buttons.
seperator = ttk.Separator(root, orient=HORIZONTAL)
seperator.place(x=0, y=50, height=10, width=10000)

# Actually run the root Loop
# Create an event loop. Keeps root in an everlasting loop, so it keeps functioning until user quits.
root.mainloop()