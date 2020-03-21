from tkinter import *
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import messagebox
import setup
import setup_3
import tkinter.scrolledtext as tkst

def back_press():
    root.destroy()
    setup.main()
    
def cancel_press():
    result = messagebox.askyesno("SOUL Setup","Are you sure you want to exit setup?")
    if (result == True):
        root.destroy()
        
def next_press():
    selection = str(var.get())
    if (selection == "1"):
        root.destroy()
        setup_3.main()
    elif(selection == "0"):
        messagebox.showwarning("SOUL Setup","Agree to the terms and conditions to continue.")
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
        backButton = Button(self, text="<< Back", command = back_press)
        backButton.pack(side=RIGHT, padx=5, pady=5)
    

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



    text2 = Text(frame, height=8, width=50)
    text3 = tkst.ScrolledText(frame, height=9, width=50)
    
    #scroll = Scrollbar(root, command=text2.yview)
    #text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Times New Roman', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Times New Roman', 16, 'bold'))
    text2.tag_configure('color', font=('Times New Roman', 11))
    text3.tag_configure('sub', font=('Times New Roman', 11))
    text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
    text2.insert(END,'\n  Terms and Conditions\n', 'big')
  
    subtitle = """
    Please read these Terms and Conditions ("Terms", "Terms
    and Conditions") carefully before using the SOUL System
    Software (the "Service") operated by TRIANGLE Group.
    """
    text2.insert(END, subtitle, 'color')
    #text2.insert(END, 'follow-up\n', 'follow')

    #scroll.pack(side=RIGHT, fill=Y)

    terms = """
   Your access to and use of the Service is conditioned on
   your acceptance of and compliance with these Terms.
   These Terms apply to all visitors, users and others who
   access or use the Service.
   By accessing or using the Service you agree to be bound
   by these Terms. If you disagree with any part of the
   terms then you may not access the Service.

   1.	Links to Other Web Sites
   Our Service may contain links to third-party web sites
   or services that are not owned or controlled by
   TRIANGLE Group.

   TRIANGLE Group has no control over, and assumes no
   responsibility for, the content, privacy policies, or
   practices of any third party web sites or services. You
   further acknowledge and agree that TRIANGLE Group
   shall not be responsible or liable, directly or indirectly,
   for any damage or loss caused or alleged to be caused by
   or in connection with use of or reliance on any such
   content, goods or services available on or through any
   such web sites or services.

   2.	Changes
   We reserve the right, at our sole discretion, to modify
   or replace these Terms at any time. If a revision is
   material we will try to provide at least 30 (change
   this) days' notice prior to any new terms taking effect.
   What constitutes a material change will be determined at
   our sole discretion.

   3.	User limit
   Who so ever acting as the end-user of SOUL System
   Software cannot misuse, pirate, sale, false market,
   false promote, hack, change the software in any
   form and by any means and doing so gives TRIANGLE
   Group the authority to take appropriate decision, including
   taking away from the organization, the culprit end user is
   working for, the right to use SOUL System from the date
   and time TRIANGLE Group decides.

   4.	Contact Us
   If you have any questions about these Terms, please
   contact us.
"""
    text1.pack(side=LEFT)
    text2.pack(side=TOP)
    text3.pack()
    text3.insert(END, terms, 'sub')
    text2.configure(state = DISABLED)

    global var
    var = IntVar()
    R1 = Checkbutton(frame, text="I agree to all the terms of the preceeding agreement.", variable=var, height = 2,justify = CENTER,padx = 60)
    R1.pack(side = LEFT)


    
    app = Example()
    #btn2.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
