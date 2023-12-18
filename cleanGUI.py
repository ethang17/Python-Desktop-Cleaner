import os
from datetime import date
typesList = [".txt", ".png",".jpeg", ".jpg", ".docx", ".doc", ".pdf", ".xlsx"]
desktopPathGlob = ""
destinationPathGlob=""

def createDir():
    baseFolderName = "DesktopCleanup--" + str(date.today())
    os.chdir(destinationPathGlob)
    os.mkdir(baseFolderName)
    os.chdir("./"+baseFolderName)
    for fileType in typesList:
        typeFolderName = fileType.strip(".")
        os.mkdir(typeFolderName)
    saveDir = os.getcwd()
    return(saveDir)


#Put file in correct folder
def sort(file, saveDir):
    splitFileName = os.path.splitext(file)
    extension = splitFileName[1]
    for fileType in typesList:
        if extension == fileType:
            os.rename(desktopPathGlob+"\\"+file,saveDir+"\\"+extension.strip(".")+"\\"+file)


def cleanUpGUI():
    saveDir = createDir()
    os.chdir(desktopPathGlob)
    for file in os.listdir():
        sort(file, saveDir)

def test():
    print("Desktop: " +desktopPathGlob)
    print("Destiantino: "+destinationPathGlob)