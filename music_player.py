# Run the code only using TERMINAL
import os
from tkinter.filedialog import askdirectory #opens up a dialogue box to add files
import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.minsize(500,300)

listofsongs = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

def nextsong(event): #the function is triggered only when event is written
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def previoussong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()

def volumeup(event):
    pygame.mixer.music.set_volume(1)

def volumedown(event):
    pygame.mixer.music.set_volume(0.3)

def pause(event):
    pygame.mixer.music.pause()

def unpause(event):
    pygame.mixer.music.unpause()

def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])
    return songlabel

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            try:
                audio = ID3(directory)
                listofsongs.append(audio['TIT2'].text[0])
            except:
                listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root,width=25,background='green')
listbox.pack()

listofsongs.reverse()

for items in listofsongs:
    listbox.insert(0,items)

nextbutton = Button(root,text='Next Song')
nextbutton.pack()

previousbutton = Button(root,text='Previous Song')
previousbutton.pack()

stopbutton = Button(root,text='Stop music')
stopbutton.pack()

volumeupbutton = Button(root,text='Volume Up')
volumeupbutton.pack()

volumedownbutton = Button(root,text='Volume Down')
volumedownbutton.pack()

pausebutton = Button(root,text='Pause')
pausebutton.pack()

unpausebutton = Button(root,text='Unpause')
unpausebutton.pack()

nextbutton.bind("<Button-1>",nextsong) #Button-1 denotes the left click of a mouse
previousbutton.bind("<Button-1>",previoussong)
stopbutton.bind("<Button-1>",stopsong)
volumeupbutton.bind("<Button-1>",volumeup)
volumedownbutton.bind("<Button-1>",volumedown)
pausebutton.bind("<Button-1>",pause)
unpausebutton.bind("<Button-1>",unpause)

songlabel.pack()

root = mainloop()
