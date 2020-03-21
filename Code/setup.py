from tkinter import *
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import messagebox
import setup_2


def cancel_press():
    result = messagebox.askyesno("SOUL Setup","Are you sure you want to exit setup?")
    if (result == True):
        root.destroy()
        
def next_press():
    root.destroy()
    setup_2.main()
    '''var = IntVar()
    R1 = Radiobutton(frame, text="Option 1", variable=var, value=1,command=sel)
    R1.pack( anchor = W )

    R2 = Radiobutton(frame, text="Option 2", variable=var, value=2,command=sel)
    R2.pack( anchor = W )

    R3 = Radiobutton(frame, text="Option 3", variable=var, value=3,command=sel)
    R3.pack( anchor = W)

    label = Label(frame)
    label.pack()

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)'''
    
class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()

        
    def initUI(self):
      
        self.master.title("SOUL Setup")
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        #frame.pack(fill=BOTH, expand=True)
        
        self.pack(fill=BOTH, expand=True)
        
        closeButton = Button(self, text="Cancel", command = cancel_press)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="Next >>", command = next_press)
        okButton.pack(side=RIGHT)
    

def main():
    global root
    root = Tk()
    root.title("SOUL Setup")
    root.iconbitmap(default = 'winicon.ico')
    root.geometry('555x380')

    frame = Frame(root)
    frame.pack()

    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM)

    text1 = Text(frame, height=20, width=21, background = "#201E1E")
    photo=PhotoImage(file='SETUP LOGO v5.png')
    text1.insert(END,'\n')
    text1.image_create(INSERT, image=photo)



    text2 = Text(frame, height=20, width=50)
    #scroll = Scrollbar(root, command=text2.yview)
    #text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Times New Roman', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Times New Roman', 20, 'bold'))
    text2.tag_configure('color', font=('Times New Roman', 12))
    text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
    text2.insert(END,'\n  SOUL System\n', 'big')
    quote = """
      This setup will guide you through the configuration of the
      system to be deployed at arrival or departure.
    """
    text2.insert(END, quote, 'color')
    #text2.insert(END, 'follow-up\n', 'follow')

    #scroll.pack(side=RIGHT, fill=Y)


    text1.pack(side=LEFT)
    text2.pack(side=LEFT)
    text2.configure(state = DISABLED)

    app = Example()
    #btn2.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
