"""from tkinter import *

ws = Tk()
ws.title("Spot")

ws.geometry("400x400")

name_variable = StringVar()


def submit():

        name = name_variable.get()

        Bonjour=Label(ws, text="Bonjour  " + name,font=('calibre', 10, 'bold'))

        Bonjour.grid(row=2, column=1)

        name_variable.set("")
def lidar():

    exec(open("..\Python370/albumention.py").read())

#def AI():
#def Posture():


Lidar_buton= Button(ws, text='Lidar', command=lidar)
AI_buton= Button(ws, text='AI')
Posture_buton= Button(ws, text='Posture')

name_label = Label(ws, text='Donner votre nom:', font=('calibre', 10, 'bold'))

name_entry = Entry(ws, textvariable=name_variable, font=('calibre', 10, 'normal'))

submit_button = Button(ws, text='Submit', command=submit)

Proposition1= Label(ws,text='taper sur: 1.Lidar',font=('calibre', 10, 'bold'))
Proposition2= Label(ws,text='2.AI',font=('calibre', 10, 'bold'))
Proposition3= Label(ws,text='3.Posture',font=('calibre', 10, 'bold'))

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
submit_button.grid(row=1, column=1)
Lidar_buton.grid(row=4,column=0)
AI_buton.grid(row=4,column=1)
Posture_buton.grid(row=4,column=2)
Proposition1.grid(row=3, column=0)
Proposition2.grid(row=3, column=1)
Proposition3.grid(row=3, column=2)


ws.mainloop()
"""
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget,QGridLayout
from PyQt5.QtGui import QImage,QBrush,QPixmap
from subprocess import Popen
app = QApplication(sys.argv)
fen = QWidget()
Title = 'SPOT Demo'
Image= 'spot.jfif'
def lidar_bouton():
    Popen("..\OneDrive - CSTC-WTCB-BBRI\Documents/testpythonbatch2.bat",shell=True)
def AI_bouton():
    print("Appui sur le bouton aussi")
def Posture_bouton():
    print("Appui sur le bouton ausssiiii")
grid= QGridLayout()

button1 = QPushButton("Lidar")
button1.clicked.connect(lidar_bouton)

button2 = QPushButton("AI")
button2.clicked.connect(AI_bouton)

button3 = QPushButton("Posture")
button3.clicked.connect(Posture_bouton)

button4 = QPushButton("Shell lidar")



grid.addWidget(button1,0,0)
grid.addWidget(button2,0,1)
grid.addWidget(button3,0,2)
grid.addWidget(button4,1,0)

fen.setStyleSheet("background-image: url("+Image+")")
fen.setGeometry(600,200,200,200)
fen.setWindowTitle(Title)
fen.setLayout(grid)
fen.show()
#..\OneDrive - CSTC-WTCB-BBRI\Pictures\images random\spot.jfif
app.exec()
