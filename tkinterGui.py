import tkinter as TK
from tkinter import filedialog
from PIL import ImageTk,Image
import cleanGUI as Clean


def browseDesktop():
    desktopP = filedialog.askdirectory()
    desktop.delete(0,'end')
    desktop.insert(0, desktopP)
    Clean.desktopPathGlob = desktopP

def browseDestination():
    destinationP = filedialog.askdirectory()
    destination.delete(0,'end')
    destination.insert(0, destinationP)
    Clean.destinationPathGlob = destinationP



root = TK.Tk()
root.geometry("500x400")
root.title("Desktop Cleanup")
root.resizable(False, False)

header = TK.Frame(root, width=500, height=75)
header.pack()

load = Image.open("GUIBanner.jpeg")
render = ImageTk.PhotoImage(load)

icon = TK.Label(header, image=render,bg="#dddddd" )
icon.pack()


body = TK.Frame(root, width=500, height=425)
body.pack()

#DESKTOP PATH FINDER Line
desktopLine = TK.Frame(body)
desktopLine.pack()

desktop = TK.Entry(desktopLine, font= ("Arial", "10"), bg="#FFFFFF", width= 50, fg = "#AAAAAA")
desktop.insert(0,"Desktop Path")
desktop.grid(row=0, column=0, padx=20, pady=20)
desktop.configure(borderwidth=0)

load2 = Image.open("Folder.png")
load2= load2.resize((15, 15))
render2 = ImageTk.PhotoImage(load2)
desktopBrowse = TK.Button(desktopLine,image=render2, bg="#DDDDDD", command=browseDesktop)
desktopBrowse.grid(row=0, column=1)

#DESTINATION PATH FINDER Line
destinationLine = TK.Frame(body)
destinationLine.pack()

destination = TK.Entry(destinationLine, font= ("Arial", "10"), bg="#FFFFFF", width= 50, fg = "#AAAAAA")
destination.insert(0,"Destination Path")
destination.grid(row=1, column=0, padx=20, pady=20)

load3 = Image.open("Folder.png")
load3= load3.resize((15, 15))
render3 = ImageTk.PhotoImage(load3)
destinationBrowse = TK.Button(destinationLine,image=render3, bg="#DDDDDD", command=browseDestination)
destinationBrowse.grid(row=1, column=1)


#Clean Desktop Button
cleanButton = TK.Button(body, width=30, height=5, command = Clean.cleanUpGUI, text="CLEAN MY DESKTOP", bg="#DDD", font=("Arial", "12", "bold"))
cleanButton.pack()


root.mainloop()
