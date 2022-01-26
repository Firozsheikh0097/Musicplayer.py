from tkinter import Label, Tk,Button,Scrollbar,Listbox,Scale,StringVar
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
import os

from pygame import mixer

root =Tk() 
listofsongs = []
songname = []
index = 0
var =StringVar()
choice=1
def prev(event=None):
    global index
    if(index==0):
        index=len(listofsongs)-1
    else:
        index=index-1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    var.set(songname[index])
def play(event=None):
    global choice
    if(choice==1):
        pygame.mixer.music.pause()
        choice=2
    else:
        pygame.mixer.music.unpause()
        choice=1
def next(event=None):
    global index
    if(index==len(listofsongs)-1):
        index=0
    else:
        index=index+1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    var.set(songname[index])
def setVolume(data):
    pygame.mixer.music.set_volume(float(data))
def setPos(data):
    pygame.mixer.music.set_pos(float(data)*60)
def selectSongs():
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir():
        realpath = os.path.realpath(files)
        audio = ID3(realpath)
        songname.append(audio["TIT2"].text[0])
        # songname.append(files)
        listofsongs.append(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    var.set(songname[0])
selectSongs()


label = Label(root,font=("Impact",20),textvariable=var)
songList = Listbox(root,font=("Impact",20))
for i in songname:
    songList.insert("end",i)
bPrev = Button(root,text="Prev",command=prev,font=("Impact",15),
                        width=10,height=2)
bPlay = Button(root,text="Play/Pause",command=play,
                        font=("Impact",15),width=10,height=2)
bNext = Button(root,text="Next",command=next,
                        font=("Impact",15),width=10,height=2)

volume = Scale(root,from_=0.0,to=1.0,resolution=0.1,command=setVolume)
volume.set(0.5)
songLength = Scale(root,from_=0.0,to=5.0,resolution=0.1,
                        orient="horizontal",length=400,
                        command=setPos)

label.grid(row=0,column=0,columnspan=5)
songList.grid(row=1,column=0,rowspan=2)
bPrev.grid(row=1,column=1)
bPlay.grid(row=1,column=2)
bNext.grid(row=1,column=3)
volume.grid(row=1,column=4)
songLength.grid(row=2,column=1,columnspan=3)

root.mainloop()