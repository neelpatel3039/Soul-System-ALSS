from tkinter import *
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import messagebox
import Departure_Window
import Arrival_Window
import homepage

#import setup_2


def cancel_press():
    #result = messagebox.askyesno("Exit Setup","Are you sure you want to exit ?")
    #if (result == True):
    write_flag()
    root.destroy()
        
def finish_press():
    if (side == "Departure"):
        write_flag()
        root.destroy()
        homepage.main()
    elif (side == "Arrival"):
        write_flag()
        root.destroy()
        homepage.main()
        
    
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

def write_flag():
    f = open("setup_needed.txt","w")
    f.write("N")
    f.close()

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
        okButton = Button(self, text="Finish", command = finish_press)
        okButton.pack(side=RIGHT)
    

def main():
    global side
    f = open("Config.txt","r")
    side = f.read()
    f.close()

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

    if (side == "Departure"):
        quote = """
        Services provided at departure side:\n
          **  Collecting fingerprints of passenger.
          **  Generating QR codes.
          **  Facility for backup.\n
        For further details, refer
        Contact us: soul.faq@gmail.com\n
        Click Finish to launch departure window.
        """
    elif (side == "Arrival"):
        quote = """
        Services provided at arrival side:\n
           **  Verifying QR codes.
           **  Taking fingerprint.
           **  Validating luggage owner.\n
        For further details, refer
        Contact us: soul.faq@gmail.com\n
        Click Finish to launch arrival window.
        """
    text2.insert(END, quote, 'color')
    #text2.insert(END, 'follow-up\n', 'follow')

    #scroll.pack(side=RIGHT, fill=Y)


    text1.pack(side=LEFT)
    text2.pack(side=LEFT)

    app = Example()
    #btn2.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
