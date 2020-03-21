#GET SCORE
#PLACE IN TEXT FILE
#AUTO_FOLDER_SEARCH

from tkinter import *
from tkinter.ttk import *
import time

def main():
    
    root=Tk()
    winWidth = 640
    winHeight = 480
    root.geometry('{}x{}'.format(winWidth, winHeight))
    root.resizable(width=False, height=False)

    bg_label = Label(root,text='Verification Status').pack()
    progress=Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
    progress['value']=5
    time.sleep(2)
    progress['value']=50
    time.sleep(2)
    progress['value']=20
    progress.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
