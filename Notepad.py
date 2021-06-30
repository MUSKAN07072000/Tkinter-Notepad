from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfilename
import os

#--------------------------------------------- DESIGNING WINDOW---------------------------------------------------------------------------------------
root = Tk()
root.geometry("400x400")
root.title("NOTEPAD")

 #--------------------------------------------- add text area------------------------------------------------------------------------------------------
textarea  = Text(root , font = "Calibri")
file = None
textarea.pack(expand = True , fill = BOTH)

 #--------------------------------------------- adding scroll bar to textarea------------------------------------------------------------------------------------------
Scroll = Scrollbar(textarea)
Scroll.pack(side = RIGHT , fill = Y)
Scroll.config(command = textarea.yview)
textarea.config(yscrollcommand = Scroll.set)

# ---------------------------------------------CREATING MAIN MENU BAR------------------------------------------------------------------------------------------
mainmenu = Menu(root)
m1 = Menu(mainmenu , tearoff = 0)
root.config(menu = mainmenu)
m2 = Menu(mainmenu , tearoff = 0)
root.config(menu = mainmenu)
m3 = Menu(mainmenu , tearoff = 0)
root.config(menu = mainmenu)

# NAMING MAIN MENU BAR
mainmenu.add_cascade(label = "File", menu = m1)
mainmenu.add_cascade(label = "Edit", menu = m2)
mainmenu.add_cascade(label = " About" , menu = m3)

# ---------------------------------------------CREATING FUNCTIONS FOR SUBMENUS------------------------------------------------------------------------------------------
#For FILE------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def New():
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0 , END)
def Open():
    global file
    file = askopenfilename(defaultextension = ".txt" , filetypes = [
        ("All Files","*.*"),
        ("Text Documents","*.txt")
    ])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        textarea.delete((1.0,END))
        f = open(file ,"r")
        textarea.insert(1.0,f.read())
        f.close()
def Save():
    global file
    #if file is new
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension = ".txt",
                                 filetypes = [("All Files","*.*"),
                                              ("TextDocuments","*.txt")])
        # if file name is not present
        if file == "":
            file = None
        #if file name is present
        else:
            f = open(file , "w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            showinfo("FileSaved")
            print("FileSaved")
    #if file is not new file
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0,END))
        f.close()
def Exit():
    root.destroy()
#For EXIT------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Cut():
    textarea.event_generate(("<<Cut>>"))
def Copy():
    textarea.event_generate(("<<Copy>>"))
def Paste():
    textarea.event_generate(("<<Paste>>"))
def Find():
    pass
#For ABOUT------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def AN():
    showinfo("Notepad","This Notepad is made for you to write ")
def AE():
    showinfo("Notepad"," This Notepad is made by Mk")

 # ---------------------------------------------CREATING SUBMENU INSIDE MAIN MENU------------------------------------------------------------------------------------------
#FOR FILE------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
m1.add_command(label = " New" , command = New  )
m1.add_command(label = " Open" , command = Open )
m1.add_command(label = " Save" , command = Save )
m1.add_command(label = " Exit" , command = Exit )
 #FOR EDIT------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
m2.add_command(label = " Cut" , command = Cut )
m2.add_command(label = " Copy" , command = Copy )
m2.add_command(label = " Paste" , command = Paste )
m2.add_command(label = " Find" , command = Find )
 #For ABOUT------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
m3.add_command(label = " About Notepad" , command = AN )
m3.add_command(label = " About Editor" , command = AE )

root.mainloop()