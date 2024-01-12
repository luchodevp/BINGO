from tkinter import *
from Extractor import Bingo
from PIL import ImageTk, Image
import tkinter as tk
import time
import copy
from tkinter import ttk
from gtts import gTTS
import os
import pyglet
import numpy as np
from tkinter import StringVar
table_color = '#F5FFFA'



def voiceMsg(value):
    msg = ""
    strValue = str(value)
    if value <= 15:
        msg = "B"
    if value > 15 and value <= 30:
        msg = "I"
    if value > 30 and value <= 45:
        msg = "N"
    if value > 45 and value <= 60:
        msg = "G"
    if value > 61 and value <= 75:
        msg = "O"
    msg = msg+strValue
    return msg


def PlaySoundBalota(VALOR):
    mytext = voiceMsg(VALOR)
    language = 'es'

    sound_produced = gTTS(text=mytext, lang=language, slow=False)
    filename = "temp.mp3"
    sound_produced.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    time.sleep(music.duration)  # prevent from killing
    os.remove(filename)  # remove temperory file


def update_seed():
    global current_time, seedLen, seed
    current_time = time.time()
    seedLen = len(str(current_time))
    seed = int(current_time)


root = Tk()
PossibleBalls = []
BalotasExtracted = []
Test = []
Lim_inf = 1
Lim_Sup = 75
Numeros = int(Lim_Sup-Lim_inf + 1)
repeated = False
Iteraciones = 0
list_index = 0
Base10 = 10**(len(str(Numeros))+1)
bg_color = '#ADD8E6'

def Changevar(value):
    global text_var
    column=0
    row_v=1
    if value <= 15:
        column=0
        row_v=1
    if value > 15 and value <= 30:
        column = 1
        row_v=16
    if value > 30 and value <= 45:
        column = 2
        row_v=31
    if value > 45 and value <= 60:
        column=3
        row_v=46
    if value > 60 and value <= 75:
        column=4
        row_v=61
    matrix = []
    for i in range (rows):
        matrix.append([])
        if (row_v==value):
                text_var[i][column].set(str(value))
        matrix[i].append(text_var[i][j].get())
        row_v=row_v+1    
    print(matrix)
def Startup():
    global PossibleBalls
    root.title('Extractor de balotas de BINGO')
    x = int(root.winfo_screenmmwidth()/2)
    y = (int(root.winfo_screenmmheight()*0.1))
    root.geometry('870x800+'+str(x)+'+'+str(y))
    root.configure(background=bg_color)
    iconLocation = 'Images/ProgramIcon.ico'
    # iconLocation='C:/Users/Luis/proyects/BINGO/Images/ProgramIcon.ico'
    root.iconbitmap(iconLocation)
    frame1 = tk.Frame(root, width=400, height=600, bg=bg_color)
    frame1.grid(row=0, column=0)
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file='Images/Logo.png')
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
             text="Estas listo para extraer una balota?",
             bg=bg_color,
             fg="black",
             font=("TkMenuFont", 14)
             ).pack()
    update_seed()
    PossibleBalls = Bingo.generateRandomNumbers(
        seed, Base10, Lim_inf, Lim_Sup, Numeros)


def ExtraerBalotaClick():
    global PossibleBalls, BalotasExtracted, Test
    ResultLabelTittle = Label(root, text="Numeros obtenidos")
    ResultLabel = Label(root, text="")
    ExtractedLabel = Label(root, text="")
    if len(PossibleBalls) <= 0:
        print("PossibleBalls is empty")
        BalotasExtracted.clear()
        ResultLabel.config(text="")
        ExtractedLabel.config(text="")
        ResultLabelTittle.config(text="")
        Test.clear()
        update_seed()
        PossibleBalls = Bingo.generateRandomNumbers(
            seed, Base10, Lim_inf, Lim_Sup, Numeros)
    ValueExtracted = PossibleBalls[0]
    Bingo.dropElementFromList(ValueExtracted, PossibleBalls, BalotasExtracted)
    Test = copy.deepcopy(BalotasExtracted)
    Test.sort()
    PlaySoundBalota(ValueExtracted)
    Changevar(ValueExtracted)

def CreateFrame1():
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file='Images/Logo.png')
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
             text="Estas listo para extraer una balota?",
             bg=bg_color,
             fg="black",
             font=("TkMenuFont", 14)
             ).pack()



Startup()
frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame1.grid(row=0, column=0)
frame2 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2.grid(row=0, column=1)
# CreateFrame1()
Load_jugar_btn = PhotoImage(file='Images/BtnJugar.png')
JugarLabel = tk.Label(image=Load_jugar_btn)
ButtonBingo = tk.Button(frame1, image=Load_jugar_btn,
                        pady=20, bg=bg_color,
                        activeforeground=bg_color,
                        cursor="hand2",
                        command=lambda: ExtraerBalotaClick(), borderwidth=0)
ButtonBingo.pack()

rows=15
cols=5
text_var=[]
entries=[]
def get_mat():
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(text_var[i][j].get())

    print(matrix)

x2=0
y2=0
for i in range(rows):
    # append an empty list to your two arrays
    # so you can append to those later
    text_var.append([])
    entries.append([])
    for j in range(cols):
        # append your StringVar and Entry
        text_var[i].append(StringVar())
        entries[i].append(Entry(frame2, textvariable=text_var[i][j],width=3))
        entries[i][j].place(x=60 + x2, y=50 + y2)
        x2 += 30

    y2 += 30
    x2 = 0
root.mainloop()

