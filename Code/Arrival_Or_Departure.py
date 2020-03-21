##-----------------------------FROM: homepage.py-----------------------------
##-----------------TO: Arrival_Window.py / Departure_Window.py---------------
##-----------------------------Importing Section-----------------------------

import Departure_Window 
import Arrival_Window   
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter

##-----------------------------Code Section----------------------------------

def jumpToArrival():
    root.destroy()
    Arrival_Window.main()
    
def jumpToDeparture():
    root.destroy()
    Departure_Window.main()
    
def main():
    
    global root
    root = Tk()
    root.title("Departure OR Arrival")
    winWidth = 640
    winHeight = 480
    root.geometry('{}x{}'.format(winWidth, winHeight))
    root.resizable(width=False, height=False)

    c = Canvas(root, bg="blue", height=480, width=640)
    filename = ImageTk.PhotoImage(Image.open("Arrival_Or_Departure.png"))
    bg_label = Label(root,image=filename)
    bg_label.place(x=0,y=0,relwidth=1,relheight=1)

    a = ttk.Button(root, text = "Departure --------->", command = jumpToDeparture)
    a.grid(column=2, columnspan=1, padx=95, pady=winHeight*0.45, ipadx=25, ipady=25, row=4, rowspan=1, sticky=W+E+S+N)
    b = ttk.Button(root, text = "---------> Arrival", command = jumpToArrival)
    b.grid(column=4, columnspan=1, padx=20, pady=winHeight*0.45, ipadx=25, ipady=25, row=4, rowspan=1, sticky=W+E+S+N)

    root.mainloop()

if __name__ == "__main__":
    main()
