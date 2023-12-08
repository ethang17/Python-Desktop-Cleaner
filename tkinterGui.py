import tkinter as TK
from tkinter import filedialog
from PIL import ImageTk,Image

root = TK.Tk()
root.geometry("500x500")
root.title("Desktop Cleanup")

header = TK.Frame(root, bg="#FF0000", width=500, height=75)

header.grid(row=0, column =0)
appTitle = TK.Label(root, text="DESKTOP CLEANUP", font=("Arial", "25", "bold"),)
appTitle.grid(row=0, column= 1)

load = Image.open("DesktopIcon.png")
load= load.resize((50,50))
render = ImageTk.PhotoImage(load)

icon = TK.Label(root, image=render)
icon.grid(row=0, column=0)
root.mainloop()
