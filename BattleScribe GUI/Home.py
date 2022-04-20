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
# Local functions
from Functions import *


root = tk.Tk()
root.title("BattleScribe Roster Editor")
root.geometry("600x600")
# This form needs a png image. This image is in the same directory currently.
root.iconphoto(False, tk.PhotoImage(file="Images\\battlescribeLogo.png"))
# For the hover text


# Sets up grid so that we can use the NSEW stretch params
root.rowconfigure(0, weight=2)
root.columnconfigure(0, weight=1)

# Grab images from a local directory (next to this .py file)
imgArrow = resizeButtonImage("Images\\arrow.png")
imgCloud = resizeButtonImage("Images\\cloud.png")
imgComputer = resizeButtonImage("Images\\computer.png")
imgComputerGear = resizeButtonImage("Images\\computerGear.png")
imgDownload = resizeButtonImage("Images\\download.png")
imgGear = resizeButtonImage("Images\\gear.png")
imgKeyboard = resizeButtonImage("Images\\keyboard.png")
imgLock = resizeButtonImage("Images\\lock.png")
imgMessage = resizeButtonImage("Images\\message.png")
imgMouse = resizeButtonImage("Images\\mouse.png")
imgSave = resizeButtonImage("Images\\save.png")
imgShieldCheck = resizeButtonImage("Images\\shieldCheck.png")
imgUpload = resizeButtonImage("Images\\upload.png")
imgSound = resizeButtonImage("Images\\sound.png")


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

# Spacing line to show separator after buttons.
# Using .place instead of grid, lets us put this separator exactly where we want based on pixels
seperator1 = ttk.Separator(root, orient=HORIZONTAL)
seperator1.place(x=0, y=50, height=10, width=10000)

seperator2 = ttk.Separator(root, orient=HORIZONTAL).grid(row=2, columnspan=15, padx=10, pady=2, sticky=EW)

dropButton1 = Button(root,  text="does this drop", width=50, height=10, command=lambda: button_clear(root))
dropButton1.grid(row=1, column=0)

# This is nearly the same as the top. Remove the rowspan
# This just creates a button spacer. The button is still in the original location
# This adds another full, separate, blank section below it.
# If you just made the original space bigger, the button and others would just spread out.
# Spacing line to show separator after buttons.
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)  # Split canvas into 3 invisible columns/rows

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