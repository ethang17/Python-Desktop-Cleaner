import tkinter as TK
from tkinter import filedialog
from PIL import ImageTk,Image
from cleanGUI import *
desktopPath=""
destinationPath=""

def browseDesktop():
    desktopPath = filedialog.askdirectory()
    desktop.delete(0,'end')
    desktop.insert(0, desktopPath)
    desktopPath = desktop.get()
#not sure if this is updating global variable or not

def browseDestination():
    destinationPath = filedialog.askdirectory()
    destination.delete(0,'end')
    destination.insert(0, destinationPath)
    destinationPath = destination.get()



root = TK.Tk()
root.geometry("500x500")
root.title("Desktop Cleanup")

header = TK.Frame(root, bg="#dddddd", width=500, height=75)
header.grid_propagate(0)
header.grid(row=0, column =0)

appTitle = TK.Label(header, text="DESKTOP CLEANUP", font=("Impact", "25"),bg="#dddddd")
appTitle.grid(row=0, column= 1, pady=10)

load = Image.open("DesktopIcon.png")
load= load.resize((50,50))
render = ImageTk.PhotoImage(load)

icon = TK.Label(header, image=render,bg="#dddddd" )
icon.grid(row=0, column=0, pady=10)


body = TK.Frame(root, width=500, height=425)
body.grid_propagate(0)
body.grid(row=1, column=0)

desktop = TK.Entry(body, font= ("Arial", "10"), bg="#FFFFFF", width= 50, fg = "#AAAAAA")
desktop.insert(0,"Desktop Path")
desktop.grid(row=0, column=0, padx=20, pady=20)
desktop.configure(borderwidth=0)

load2 = Image.open("Folder.png")
load2= load2.resize((15, 15))
render2 = ImageTk.PhotoImage(load2)
desktopBrowse = TK.Button(body,image=render2, bg="#DDDDDD", command=browseDesktop)
desktopBrowse.grid(row=0, column=1)

load3 = Image.open("Folder.png")
load3= load3.resize((15, 15))
render3 = ImageTk.PhotoImage(load3)
saveBrowse = TK.Button(body,image=render3, bg="#DDDDDD", command=browseDestination)
saveBrowse.grid(row=1, column=1)


destination = TK.Entry(body, font= ("Arial", "10"), bg="#FFFFFF", width= 50, fg = "#AAAAAA")
destination.insert(0,"Destination Path")
destination.grid(row=1, column=0, padx=20, pady=20)


#need to add funciton from other file as command=
cleanButton = TK.Button(body, width=40, height=10, text=desktopPath)
cleanButton.grid(row=2, column=0)


root.mainloop()
