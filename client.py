import socket
from tkinter import *
import pygame
from pygame import mixer
import os
from PIL import ImageTk

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 8050
BUFFER_SIZE = 4096

name = None
listbox =  None
filePathLabel = None
is_Pause = False

global song_counter
song_counter = 0

window = Tk()

def resume():
    global song_selected

    pygame
    mixer.init()
    
    mixer.music.load('shared_files/'+song_selected)
    pygame.mixer.music.play()
    PlayButton.configure(text = "\u23F8", command=pause)
    infoLabel.configure(text="Resumed: " +song_selected)

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="Paused: " +song_selected)
    PlayButton.configure(text = "\u23F5", command=resume)

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)

    if len(song_selected) == 0:
        infoLabel.configure(text='Please select a song.')
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: " +song_selected)
    else:
       infoLabel.configure(text="")
    PlayButton.configure(text = "\u23F8", command=pause)

def stop():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")
    PlayButton.configure(text = "\u23F5", command=play)

def musicWindow():
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel
    global PlayButton

    window.title('Music Sharer')
    window.resizable(width=False,height=False)
    window.geometry('540x490')
    window.configure(bg='#202121')

    selectlabel = Label(window, text= "Select Song",bg="#202121" ,fg="white",font = ("Calibri 24 bold"))
    selectlabel.place (x=6, y=4)

    listbox = Listbox(window , height = 13,width = 51, activestyle = "dotbox" , bg='#495057',fg = '#fff', bd=0 ,highlightthickness=3,font = ("calibri" , 14))
    listbox.place (x=10,y=45)
    listbox.config(cursor='arrow',highlightbackground = "#2ec4b6", highlightcolor= "#2ec4b6")

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1
        
    if song_counter == 0:
        img = ImageTk.PhotoImage(file = "./assets/delete.png")
        
        canvas = Canvas( window, width = 200,height = 200,bg="#495057",highlightcolor= "#2ec4b6",highlightthickness=0, relief='ridge')
        canvas.pack( expand = False)
        canvas.create_image( 50,50, image = img, anchor = "nw")
        canvas.grid(padx=190, pady=90)

        alert = Label(window,text="Could not find any songs.",fg='white',bg="#495057",font = ("calibri" , 14))
        alert.place(x=180,y=210)
  
    scrollbarl = Scrollbar(listbox)
    scrollbarl.place(relheight= 1,relx= 0.965)
    scrollbarl.config(command= listbox.yview)

    infoLabel = Label(window, text= "",bg="#202121",fg= "#2ec4b6", font = ("Calibri 14 italic") )
    infoLabel.place (x=6, y=460)

    PlayButton = Button(window,text='\u23F5', bd=0, bg="#202121",fg='#2ec4b6' , font= ("calibri 32 bold"),command=play)
    PlayButton.place (x=200, y=375)
    
    Stop = Button(window, text="⏹", bd=0 , bg="#202121",fg='#2ec4b6', font = ("calibri 48 bold",),command=stop)
    Stop.place (x=270, y=405)

    Upload = Button(window, text="Upload", width=5,bg="#202121",fg='#2ec4b6',bd=0, font= ("calibri 14 bold"))
    Upload.place (x=130,y=400)

    Download = Button(window , text="Download",width=8,bg="#202121",fg='#2ec4b6',bd=0, font= ("calibri 14 bold"))
    Download.place(x=320, y=400)

    window.mainloop ()

def setup():
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    print('\t\t\t\tCONNECTED')

    musicWindow()

setup()