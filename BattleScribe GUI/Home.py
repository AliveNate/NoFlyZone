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


# Simple function just as placeholder currently.
def button_clear():
    # Creates entry box just to have code in here. Not good for this function.
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    # Clear the text from the box
    e.delete(0, END)


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
button_NoFlyZone            = Button(root, text="NoFlyZone.com",  bg="#112637", fg="White", padx=10, pady=10, command=button_clear)
button_CreateNewRoster      = Button(root, image=imgKeyboard, bg="#112637", fg="White", padx=12, pady=10, command=button_clear)
button_OpenExistingRoster   = Button(root, image=imgArrow, bg="#112637", fg="White", padx=12, pady=10, command=button_clear)
button_OpenRosterToView     = Button(root, image=imgDownload, bg="#112637", fg="White", padx=12, pady=10, command=button_clear)
button_SaveTheRoster        = Button(root, image=imgUpload, bg="#112637", fg="White", padx=11, pady=10, command=button_clear)
button_SaveTheRosterAs      = Button(root, image=imgSave, bg="#112637", fg="White", padx=11, pady=10, command=button_clear)
button_ViewTheRoster        = Button(root, image=imgComputer, bg="#112637", fg="White", padx=11, pady=10, command=button_clear)
button_ShareTheRoster       = Button(root, image=imgCloud, bg="#112637", fg="White", padx=11, pady=10, command=button_clear)
button_PrintTheRoster       = Button(root, image=imgLock, bg="#112637", fg="White", padx=11, pady=10, command=button_clear)
button_ManageData           = Button(root, image=imgComputerGear, bg="#112637", fg="White", padx=11, pady=10, command=button_clear)
button_SupportBattleScribe  = Button(root, image=imgShieldCheck, bg="#112637", fg="White", padx=11, pady=10, command=button_clear)
button_DiceTool             = Button(root, image=imgGear, bg="#112637", fg="White", padx=11, pady=10, command=button_clear)
button_Updates              = Button(root, image=imgSound, bg="#112637", fg="White", padx=10, pady=10, command=button_clear)
button_ReportABug           = Button(root, image=imgMessage, bg="#112637", fg="White", padx=10, pady=10, command=button_clear)



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