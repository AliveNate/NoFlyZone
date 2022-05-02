import tkinter as tk
from tkinter import *
from tkinter import ttk
# Adjusting PDF files
# python3 -m pip install --upgrade PyPDF3
import Pmw.Pmw_2_0_1.lib.PmwBase
import PyPDF2
# Work with images
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow
from PIL import Image, ImageTk
# To let us browse/open a file after button click.
from tkinter.filedialog import askopenfile
# Hover tip balloon messages
from idlelib.tooltip import Hovertip
from numpy import *
import numpy as np
# Local functions
from Functions import *

# Get the current working directory for further target sub addresses
import os
cwd = os.getcwd()

root = tk.Tk()
root.title("BattleScribe Roster Editor")
root.geometry("680x600")
# This form needs a png image. This image is in the same directory currently.
root.iconphoto(False, tk.PhotoImage(file=cwd + "\\Images\\battlescribeLogo.png"))
# For the hover text


# Sets up grid so that we can use the NSEW stretch params
root.rowconfigure(0, weight=2)
root.columnconfigure(0, weight=1)

# Grab images from a local directory (next to this .py file)
imgArrow = resizeButtonImage(cwd + "\\Images\\arrow.png")
imgCloud = resizeButtonImage(cwd + "\\Images\\cloud.png")
imgComputer = resizeButtonImage(cwd + "\\Images\\computer.png")
imgComputerGear = resizeButtonImage(cwd + "\\Images\\computerGear.png")
imgDownload = resizeButtonImage(cwd + "\\Images\\download.png")
imgGear = resizeButtonImage(cwd + "\\Images\\gear.png")
imgKeyboard = resizeButtonImage(cwd + "\\Images\\keyboard.png")
imgLock = resizeButtonImage(cwd + "\\Images\\lock.png")
imgMessage = resizeButtonImage(cwd + "\\Images\\message.png")
imgMouse = resizeButtonImage(cwd + "\\Images\\mouse.png")
imgSave = resizeButtonImage(cwd + "\\Images\\save.png")
imgShieldCheck = resizeButtonImage(cwd + "\\Images\\shieldCheck.png")
imgUpload = resizeButtonImage(cwd + "\\Images\\upload.png")
imgSound = resizeButtonImage(cwd + "\\Images\\sound.png")


# Use  lambda to pass a var/value to a button function (command=lambda: button_click(1)))
button_NoFlyZone            = Button(root, text="NoFlyZone.com",  bg="#112637", fg="White", padx=10, pady=10, command=lambda: button_clear(root))
button_CreateNewRoster      = Button(root, image=imgKeyboard, bg="#112637", fg="White", padx=12, pady=10, command=lambda: button_clear(root))
button_OpenExistingRoster   = Button(root, image=imgArrow, bg="#112637", fg="White", padx=12, pady=10, command=lambda: button_clear(root))
button_OpenRosterToView     = Button(root, image=imgDownload, bg="#112637", fg="White", padx=12, pady=10, command=lambda: button_clear(root))
button_SaveTheRoster        = Button(root, image=imgUpload, bg="#112637", fg="White", padx=11, pady=10, command=lambda: button_clear(root))
button_SaveTheRosterAs      = Button(root, image=imgSave, bg="#112637", fg="White", padx=11, pady=10, command=lambda: button_clear(root))
button_ViewTheRoster        = Button(root, image=imgComputer, bg="#112637", fg="White", padx=11, pady=10, command=lambda: button_clear(root))
button_ShareTheRoster       = Button(root, image=imgCloud, bg="#112637", fg="White", padx=11, pady=10, command=lambda: button_clear(root))
button_PrintTheRoster       = Button(root, image=imgLock, bg="#112637", fg="White", padx=11, pady=10, command=lambda: button_clear(root))
button_ManageData           = Button(root, image=imgComputerGear, bg="#112637", fg="White", padx=11, pady=10, command=lambda: button_clear(root))
button_SupportBattleScribe  = Button(root, image=imgShieldCheck, bg="#112637", fg="White", padx=11, pady=10, command=lambda: button_clear(root))
button_DiceTool             = Button(root, image=imgGear, bg="#112637", fg="White", padx=11, pady=10, command=lambda: button_clear(root))
button_Updates              = Button(root, image=imgSound, bg="#112637", fg="White", padx=10, pady=10, command=lambda: button_clear(root))
button_ReportABug           = Button(root, image=imgMessage, bg="#112637", fg="White", padx=10, pady=10, command=lambda: button_clear(root))


# Button has hover message
# Button has colorado change on hover, BUT...
# Cannot get hover color change, and message popup at the same time. Not sure why
myTip1 = Hovertip(button_NoFlyZone, 'This is a \n multiline tip')
myTip2 = Hovertip(button_CreateNewRoster, 'Create a new roster')
myTip3 = Hovertip(button_OpenExistingRoster, 'Open existing roster')
myTip4 = Hovertip(button_OpenRosterToView, 'Open roster to view')
myTip5 = Hovertip(button_SaveTheRoster, 'Save the roster')
myTip6 = Hovertip(button_SaveTheRosterAs, 'Save the roster as')
myTip7 = Hovertip(button_ViewTheRoster, 'View the roster')
myTip8 = Hovertip(button_ShareTheRoster, 'Share the roster')
myTip9 = Hovertip(button_PrintTheRoster, 'Print the roster')
myTip10 = Hovertip(button_ManageData, 'Manage data')
myTip11 = Hovertip(button_SupportBattleScribe, 'Support BattleScribe')
myTip12 = Hovertip(button_DiceTool, 'Dice Tool')
myTip13 = Hovertip(button_Updates, 'Application Updates')
myTip14 = Hovertip(button_ReportABug, 'Report a bug')

'''
# Change color of buttons when you hover over, and the back to original when you move away
# This works BUT does not work along with the hover text
changeOnHover(button_NoFlyZone, "Dark Red", "#112637")
changeOnHover(button_CreateNewRoster, "Dark Red", "#112637")
changeOnHover(button_OpenExistingRoster, "Dark Red", "#112637")
changeOnHover(button_OpenRosterToView, "Dark Red", "#112637")
changeOnHover(button_SaveTheRoster, "Dark Red", "#112637")
changeOnHover(button_SaveTheRosterAs, "Dark Red", "#112637")
changeOnHover(button_ViewTheRoster, "Dark Red", "#112637")
changeOnHover(button_ShareTheRoster, "Dark Red", "#112637")
changeOnHover(button_PrintTheRoster, "Dark Red", "#112637")
changeOnHover(button_ManageData, "Dark Red", "#112637")
changeOnHover(button_SupportBattleScribe, "Dark Red", "#112637")
changeOnHover(button_DiceTool, "Dark Red", "#112637")
changeOnHover(button_Updates, "Dark Red", "#112637")
changeOnHover(button_ReportABug, "Dark Red", "#112637")
'''

# Put buttons on the screen
# sticky="NSEW"  Lets us stretch items if the window gets bigger in real time.
button_NoFlyZone.grid(          row=0, column=0, sticky="NEW")
button_CreateNewRoster.grid(    row=0, column=1, sticky="NEW")
button_OpenExistingRoster.grid( row=0, column=2, sticky="NEW")
button_OpenRosterToView.grid(   row=0, column=3, sticky="NEW")
button_SaveTheRoster.grid(      row=0, column=4, sticky="NEW")
button_SaveTheRosterAs.grid(    row=0, column=5, sticky="NEW")
button_ViewTheRoster.grid(      row=0, column=6, sticky="NEW")
button_ShareTheRoster.grid(     row=0, column=7, sticky="NEW")
button_PrintTheRoster.grid(     row=0, column=8, sticky="NEW")
button_ManageData.grid(         row=0, column=9, sticky="NEW")
button_SupportBattleScribe.grid(row=0, column=10, sticky="NEW")
button_DiceTool.grid(           row=0, column=11, sticky="NEW")
button_Updates.grid(            row=0, column=12, sticky="NEW")
button_ReportABug.grid(         row=0, column=13, sticky="NEW")

# Top separator after the buttons
leftBorder = ttk.Separator(root, orient=VERTICAL)
leftBorder.place(x=0, height=1000, width=5)
# Line just below the top buttons
seperator1 = ttk.Separator(root, orient=HORIZONTAL)
seperator1.place(x=5, y=50, height=100, width=10000)
# ------------------------------------------------------------------------
# 3 buttons/labels on the second section.
# Press the + and it expands, - and it retracts
# Command should be a function that expands or retracts
# ----------- First  top +/- button label
# List is created for a button. Then each list is placed in an array.
# 00 = first row, first button,   01 = first row, second button
# Button lists = [arrayPosition, name, symbol, xbutton, xLabel, yPosition, buttonArrayPos]
btnLst00 = [0, "dropBtn00", "+", 5, 25, 51]
btnLst01 = [0, "dropBtn01", "+", 230, 250, 51]
btnLst02 = [0, "dropBtn02", "+", 455, 475, 51]
# Array of lists. Send and append each time a new button/label is created.
# If button in position3 is minimized, then we can also minimize each position after that also
btnLstAry0 = [btnLst00]
btnLstAry1 = [btnLst01]
btnLstAry2 = [btnLst02]
# -----------------------------
dropBtn00 = Button(root,  text="+", command=lambda: dropDownOneSection(root, dropBtn00, btnLstAry0, 0), relief=FLAT, background="gray")
dropBtn00.place(x=5, y=51, height=40, width=20)
lbl00 = Label(root, text="Here is the first input", borderwidth=1, relief="solid")
lbl00.place(x=25, y=51, height=40, width=200)
# ---------- Second top +/- button label
dropBtn01 = Button(root,  text="+", command=lambda: dropDownOneSection(root, dropBtn01, btnLstAry1, 0), relief=FLAT, background="gray")
dropBtn01.place(x=230, y=51, height=40, width=20)
lbl01 = Label(root, text="Here is the first input", borderwidth=1, relief="solid")
lbl01.place(x=250, y=51, height=40, width=200)
# ----------Third top +/- button label
dropBtn02 = Button(root,  text="+", command=lambda: dropDownOneSection(root, dropBtn02, btnLstAry2, 0), relief=FLAT, background="gray")
dropBtn02.place(x=455, y=51, height=40, width=20)
lbl02 = Label(root, text="Here is the first input", borderwidth=1, relief="solid")
lbl02.place(x=475, y=51, height=40, width=200)
# -------------------------------------------------------------------------
# Spacing line to show separator after buttons.
# Using .place instead of grid, lets us put this separator exactly where we want based on pixels
seperator2 = ttk.Separator(root, orient=HORIZONTAL)
seperator2.place(x=1, y=200, height=1, width=10000)


# This is nearly the same as the top. Remove the rowspan
# This just creates a button spacer. The button is still in the original location
# This adds another full, separate, blank section below it.
# If you just made the original space bigger, the button and others would just spread out.
# Spacing line to show separator after buttons.
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=13)  # Split canvas into 3 invisible columns/rows

# Actually run the root Loop
# Create an event loop. Keeps root in an everlasting loop, so it keeps functioning until user quits.
root.mainloop()

'''
     0      1      2      3      4      5      6      7      8      9       10      11      12      13              
0  btn1 | btn2 | btn3 | btn4 | btn5 | btn6 | btn7 | btn8 | btn9 | btn10 | btn11 | btn12 | btn13 | btn14
   ----------------------------------------------------------------------------------------------------
1

2

3

4

5

6

7

8

9

10

11

12

13
'''