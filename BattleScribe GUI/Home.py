from tkinter import *
from tkinter import ttk

gui = Tk()
gui.title("BattleScribe")
gui.geometry("600x600")



def button_clear():
    # Creates entry box just to have code in here. Not good for this function.
    e = Entry(gui, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    # Clear the text from the box
    e.delete(0, END)

# Sets up grid so we can use the NSEW stretch params
Grid.rowconfigure(gui, 0, weight=1)
Grid.columnconfigure(gui, 0, weight=1)

# Use  lambda to pass a var/value to a button function (command=lambda: button_click(1)))
button_CreateNewRoster      = Button(gui, text="1", padx=10, pady=10, command=button_clear)
button_OpenExistingRoster   = Button(gui, text="2", padx=10, pady=10, command=button_clear)
button_OpenRosterToView     = Button(gui, text="3", padx=10, pady=10, command=button_clear)
button_SaveTheRoster        = Button(gui, text="4", padx=10, pady=10, command=button_clear)
button_SaveTheRosterAs      = Button(gui, text="5", padx=10, pady=10, command=button_clear)
button_ViewTheRoster        = Button(gui, text="6", padx=10, pady=10, command=button_clear)
button_ShareTheRoster       = Button(gui, text="7", padx=10, pady=10, command=button_clear)
button_PrintTheRoster       = Button(gui, text="8", padx=10, pady=10, command=button_clear)
button_ManageData           = Button(gui, text="9", padx=10, pady=10, command=button_clear)
button_SupportBattleScribe  = Button(gui, text="10", padx=10, pady=10, command=button_clear)
button_DiceTool             = Button(gui, text="11", padx=10, pady=10, command=button_clear)
button_Updates              = Button(gui, text="12", padx=10, pady=10, command=button_clear)
button_ReportABug           = Button(gui, text="13", padx=10, pady=10, command=button_clear)

# Put buttons on the screen
# sticky="NSEW"  Lets us stretch items if the window gets bigger in real time.
button_CreateNewRoster.grid(row=0, column=0, sticky="NEW")
button_OpenExistingRoster.grid(row=0, column=1, sticky="NEW")
button_OpenRosterToView.grid(row=0, column=2, sticky="NEW")
button_SaveTheRoster.grid(row=0, column=3, sticky="NEW")
button_SaveTheRosterAs.grid(row=0, column=4, sticky="NEW")
button_ViewTheRoster.grid(row=0, column=5, sticky="NEW")
button_ShareTheRoster.grid(row=0, column=6, sticky="NEW")
button_PrintTheRoster.grid(row=0, column=7, sticky="NEW")
button_ManageData.grid(row=0, column=8, sticky="NEW")
button_SupportBattleScribe.grid(row=0, column=9, sticky="NEW")
button_DiceTool.grid(row=0, column=10, sticky="NEW")
button_Updates.grid(row=0, column=11, sticky="NEW")
button_ReportABug.grid(row=0, column=12, sticky="NEW")


seperator = ttk.Separator(gui, orient=HORIZONTAL)
seperator.place(x=0, y=50, height=10, width=10000)


# Actually run the GUI Loop
# Create an event loop. Keeps GUI in an everlasting loop, so it keeps functioning until user quits.
gui.mainloop()