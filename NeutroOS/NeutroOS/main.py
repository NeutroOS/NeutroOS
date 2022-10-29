from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()
p1 = PhotoImage(file='NeutroOSicon.png')
root.title('Neutros Operating System')
root.iconphoto(False, p1)
root.geometry("800x400")


def neutrotext():
    os.system('cmd /c /NeutroOS/NeutroText/main.py')

def neutronet():
    os.system('cmd /c /NeutroOS/NeutroNet/main.py')

def neutroart():
    os.system('cmd /c /NeutroOS/NeutroArt/main.py')

def neutromath():
    os.system('cmd /c /NeutroOS/NeutroMath/main.py')

def neutroterminal():
    os.system('cmd /c /NeutroOS/NeutroTerminal/main.py')

def neutrohelp():
    os.system('cmd /c /NeutroOS/NeutroHelp/main.py')






#Opening
NeutroTextPhoto = Image.open('NeutroText/NeutroTexticon.png')
NeutroNetPhoto = Image.open('NeutroNet/NeutroNeticon.png')
NeutroArtPhoto = Image.open('NeutroArt/NeutroArticon.png')
NeutroMathPhoto = Image.open('NeutroMath/NeutroMathicon.png')
NeutroTerminalPhoto = Image.open('NeutroTerminal/NeutroTerminalicon.png')
NeutroHelpPhoto = Image.open('NeutroHelp/NeutroHelpicon.png')






#Resize images
NeutroTextPhotoresized = NeutroTextPhoto.resize((60, 60), Image.Resampling.LANCZOS)
NeutroTextPhotores = ImageTk.PhotoImage(NeutroTextPhotoresized)
NeutroNetPhotoresized = NeutroNetPhoto.resize((60, 60), Image.Resampling.LANCZOS)
NeutroNetPhotores = ImageTk.PhotoImage(NeutroNetPhotoresized)
NeutroArtPhotoresized = NeutroArtPhoto.resize((60, 60), Image.Resampling.LANCZOS)
NeutroArtPhotores = ImageTk.PhotoImage(NeutroArtPhotoresized)
NeutroMathPhotoresized = NeutroMathPhoto.resize((60, 60), Image.Resampling.LANCZOS)
NeutroMathPhotores = ImageTk.PhotoImage(NeutroMathPhotoresized)
NeutroTerminalPhotoresized = NeutroTerminalPhoto.resize((60, 60), Image.Resampling.LANCZOS)
NeutroTerminalPhotores = ImageTk.PhotoImage(NeutroTerminalPhotoresized)
NeutroHelpPhotoresized = NeutroHelpPhoto.resize((60, 60), Image.Resampling.LANCZOS)
NeutroHelpPhotores = ImageTk.PhotoImage(NeutroHelpPhotoresized)


#Photos
NeutroTextPhoto = ImageTk.PhotoImage(file='NeutroText/NeutroTexticon.png')
NeutroNetPhoto = ImageTk.PhotoImage(file='NeutroNet/NeutroNeticon.png')
NeutroArtPhoto = ImageTk.PhotoImage(file='NeutroArt/NeutroArticon.png')
NeutroMathPhoto = ImageTk.PhotoImage(file='NeutroMath/NeutroMathicon.png')
NeutroTerminalPhoto = ImageTk.PhotoImage(file='NeutroTerminal/NeutroTerminalicon.png')
NeutroHelpPhoto = ImageTk.PhotoImage(file='NeutroHelp/NeutroHelpicon.png')








#Labels
Mainheader = Label(text="Welcome to NeutroOS", font='Verdana 12 bold', fg="#66B2FF")
Mainheader.pack()
Mainheader2 = Label(text="the best and easiest to use collection of applications out there, click on NeutroHelp", font='Verdana 12 bold', fg="#66B2FF")
Mainheader2.pack()
Mainheader3 = Label(text="to get started.", font='Verdana 12 bold', fg="#66B2FF")
Mainheader3.pack()
neutrotextphoto = Label(image=NeutroTextPhoto)
neutronetphoto = Label(image=NeutroNetPhoto)
neutrotextlabel = Label(text="NeutroText")
neutrotextlabel.pack()
neutrotextlabel.place(x=5, y=150)
neutronetlabel = Label(text="NeutroNet")
neutronetlabel.pack()
neutronetlabel.place(x=100, y=150)
neutroartphoto = Label(image=NeutroArtPhoto)
neutroartlabel = Label(text="NeutroArt")
neutroartlabel.pack()
neutroartlabel.place(x=195, y=150)
neutromathphoto = Label(image=NeutroMathPhoto)
neutromathlabel = Label(text="NeutroMath")
neutromathlabel.pack()
neutromathlabel.place(x=290, y=150)
neutroterminalphoto = Label(image=NeutroTerminalPhoto)
neutroterminallabel = Label(text="NeutroTerminal")
neutroterminallabel.pack()
neutroterminallabel.place(x=385, y=150)
neutrohelpphoto = Label(image=NeutroHelpPhoto)
neutrohelplabel = Label(text="NeutroHelp")
neutrohelplabel.pack()
neutrohelplabel.place(x=480, y=150)



#Buttons
NeutroTextButton = Button(root, image=NeutroTextPhotores, command=neutrotext)
NeutroTextButton.pack()
NeutroTextButton.place(x=5, y=80)
NeutroNetButton = Button(root, image=NeutroNetPhotores, command=neutronet)
NeutroNetButton.pack()
NeutroNetButton.place(x=100, y=80)
NeutroArtButton = Button(root, image=NeutroArtPhotores, command=neutroart)
NeutroArtButton.pack()
NeutroArtButton.place(x=195, y=80)
NeutroMathButton = Button(root, image=NeutroMathPhotores, command=neutromath)
NeutroMathButton.pack()
NeutroMathButton.place(x=290, y=80)
NeutroTerminalButton = Button(root, image=NeutroTerminalPhotores, command=neutroterminal)
NeutroTerminalButton.pack()
NeutroTerminalButton.place(x=385, y=80)
NeutroHelpButton = Button(root, image=NeutroHelpPhotores, command=neutrohelp)
NeutroHelpButton.pack()
NeutroHelpButton.place(x=480, y=80)



root.mainloop()