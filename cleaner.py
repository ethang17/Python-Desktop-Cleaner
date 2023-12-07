
import os
from datetime import date

typesList = [".txt", ".png",".jpeg", ".jpg", ".docx", ".doc", ".pdf"]
desktopDir = "C:\\Users\\16103\\OneDrive\\Desktop"

#Make Cleanup folder and type files
def createDir():
    baseFolderName = "DesktopCleanup--" + str(date.today())
    os.chdir("C:\\Users\\16103\\OneDrive")
    os.mkdir(baseFolderName)
    os.chdir(".\\"+baseFolderName)
    for fileType in typesList:
        typeFolderName = fileType.strip(".")
        os.mkdir(typeFolderName)
    saveDir = os.getcwd()
    return(saveDir)

#Put file in correct folder
def sort(file, saveDir):
    splitFileName = os.path.splitext(file)
    nakedFileName = splitFileName[0]
    extension = splitFileName[1]
    for fileType in typesList:
        if extension == fileType:
            os.rename(desktopDir+"\\"+file,saveDir+"\\"+extension.strip(".")+"\\"+file)


if __name__ == "__main__":
    saveDir = createDir()
    print(saveDir)
    os.chdir(desktopDir)
    for file in os.listdir():
        sort(file, saveDir)

