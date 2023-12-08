
import os
from datetime import date

typesList = [".txt", ".png",".jpeg", ".jpg", ".docx", ".doc", ".pdf", ".xlsx"]
userHome =os.path.expanduser('~')
desktopDir = ""
oneDriveName = ""


def findOneDrive():
    validInput= False
    oneDriveName = ""
    while validInput == False:
        print("Does your OneDrive have a special name? Y/N")    
        userInput = input()
        match(userInput.upper()):
            case "Y":
                while validInput == False:
                    print("What is the name of your OneDrive Folder?")
                    try:
                        oneDriveName = input()
                        os.chdir(userHome+"\\"+oneDriveName)
                        validInput = True
                    except:
                        print("That is not a valid directory in your user profile. Try again.")

            case "N":
                oneDriveName = "OneDrive"
                validInput = True
            case _:
                print("Please respond Y or N")
    return oneDriveName




#Make Cleanup folder and type files
def createDir():
    baseFolderName = "DesktopCleanup--" + str(date.today())
    os.chdir(userHome+"\\"+oneDriveName)
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
    extension = splitFileName[1]
    for fileType in typesList:
        if extension == fileType:
            os.rename(desktopDir+"\\"+file,saveDir+"\\"+extension.strip(".")+"\\"+file)


if __name__ == "__main__":
    oneDriveName = findOneDrive()
    desktopDir = userHome +"\\"+oneDriveName+"\\Desktop"
    saveDir = createDir()
    print(saveDir)
    os.chdir(desktopDir)
    for file in os.listdir():
        sort(file, saveDir)

