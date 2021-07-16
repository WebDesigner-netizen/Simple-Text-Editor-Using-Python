# Importing Required libraries & Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
# Defining TextEditor Class
class TextEditor:
  # Defining Constructor
  def __init__(self,root):
    # Assigning root
    self.root = root
    self.root.title("Sayak's Text Editor")
    self.root.geometry("1200x700+200+150")
    self.filename = None
    self.title = StringVar()
    self.status = StringVar()
    self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",12,"normal"),foreground="#969eac",background="#21252b",bd=2,relief=RAISED)
    self.titlebar.pack(side=TOP,fill=BOTH)
    self.settitle()
    self.statusbar = Label(self.root,textvariable=self.status,font=("Comic Sans MS",15,"bold"),foreground="#969eac",background="#21252b",bd=1,relief=GROOVE)
    self.statusbar.pack(side=BOTTOM,fill=BOTH)
    
    # Initializing Status
    self.status.set("Welcome To My Simple Text Editor")
    
    # Creating Menubar
    self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="#ffffff")
    # Configuring menubar on root window
    self.root.config(menu=self.menubar)
    # Creating File Menu
    self.filemenu = Menu(self.menubar,font=("times new roman",12,"normal"),activeforeground='#000000',activebackground="#e6e6e6",tearoff=0)
    self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
    self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
    self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
    self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
    
    # Adding Seprator
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
    # Cascading filemenu to menubar
    self.menubar.add_cascade(label="File", menu=self.filemenu)
    
    # Creating Edit Menu
    self.editmenu = Menu(self.menubar,font=("times new roman",12,"normal"),activeforeground='#000000',activebackground="#e6e6e6",tearoff=0)
    self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
    self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
    self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)

    #Not Functional
    self.editmenu.add_command(label="Select All")
    self.editmenu.add_command(label="Find")
    self.editmenu.add_command(label="Replace")


    # Adding Seprator
    self.editmenu.add_separator()
    # Adding Undo text Command
    self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)


    # Adding Redo text command(Not Functional)
    self.editmenu.add_command(label="Redo")


    # Cascading editmenu to menubar
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)
    # Creating Help Menu
    self.helpmenu = Menu(self.menubar,font=("times new roman",12,"normal"),activeforeground='#000000',activebackground="#e6e6e6",tearoff=0)
    self.helpmenu.add_command(label="About",command=self.infoabout)
    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)


    # Creating Format Menu
    self.formatmenu = Menu(self.menubar,font=("times new roman",12,"normal"),activeforeground='#000000',activebackground="#e6e6e6",tearoff=0)
    self.formatmenu.add_command(label="Word Wrap",command=self.infoabout)
    self.formatmenu.add_command(label="Font",command=self.infoabout)
    self.menubar.add_cascade(label="Format", menu=self.formatmenu)


    # Creating Scrollbar
    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    # Creating Text Area
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",14,"normal"),insertbackground="#558dff",foreground="#c5cad3",background="#282c34",state="normal",relief=GROOVE)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.txtarea.yview)
    self.txtarea.pack(fill=BOTH,expand=1)
    self.shortcuts()
    
  # Defining settitle function
  def settitle(self):
    # Checking if Filename is not None
    if self.filename:
      # Updating Title as filename
      self.title.set(self.filename)
    else:
      # Updating Title as Untitled
      self.title.set("Untitled")
  # Defining New file Function
  def newfile(self,*args):
    # Clearing the Text Area
    self.txtarea.delete("1.0",END)
    self.filename = None
    self.settitle()
    self.status.set("New File Created Successfully")
    
  def openfile(self,*args):
    # Exception handling
    try:
      # Asking for file to open
      self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      if self.filename:
        infile = open(self.filename,"r")
        # Clearing text area
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        infile.close()
        self.settitle()
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)
      
  # Defining Save File Funtion
  def savefile(self,*args):
    try:
      if self.filename:
        data = self.txtarea.get("1.0",END)
        outfile = open(self.filename,"w")
        outfile.write(data)
        outfile.close()
        self.settitle()
        self.status.set("Saved Successfully")
      else:
        self.saveasfile()
    except Exception as e:
      messagebox.showerror("Exception",e)
      
  # Defining Save As File Funtion
  def saveasfile(self,*args):
    try:
      untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      data = self.txtarea.get("1.0",END)
      outfile = open(untitledfile,"w")
      outfile.write(data)
      outfile.close()
      self.filename = untitledfile
      self.settitle()
      self.status.set("Saved Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

      
  def exit(self,*args):
    op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!")
    if op>0:
      self.root.destroy()
    else:
      return
    
  # Defining Cut Funtion
  def cut(self,*args):
    self.txtarea.event_generate("<<Cut>>")
    
  # Defining Copy Funtion
  def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")
      
  # Defining Paste Funtion
  def paste(self,*args):
    self.txtarea.event_generate("<<Paste>>")
    
  # Defining Undo Funtion
  def undo(self,*args):
    try:
      if self.filename:
        self.txtarea.delete("1.0",END)
        infile = open(self.filename,"r")
        for line in infile:
          self.txtarea.insert(END,line)
        infile.close()
        self.settitle()
        self.status.set("Undone Successfully")
      else:
        self.txtarea.delete("1.0",END)
        self.filename = None
        self.settitle()
        self.status.set("Undone Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)
  def infoabout(self):
    messagebox.showinfo("About Text Editor","A Simple Text Editor\nCreated using Python\nBy Sayak Ghosh(16th July,2021).")



#def wordwrap(self,t):
    #t = Text(wrap=WORD)
    #t.pack()

  # Defining shortcuts Funtion
  def shortcuts(self):
    self.txtarea.bind("<Control-n>",self.newfile)
    self.txtarea.bind("<Control-o>",self.openfile)
    self.txtarea.bind("<Control-s>",self.savefile)
    self.txtarea.bind("<Control-a>",self.saveasfile)
    self.txtarea.bind("<Control-e>",self.exit)
    self.txtarea.bind("<Control-x>",self.cut)
    self.txtarea.bind("<Control-c>",self.copy)
    self.txtarea.bind("<Control-v>",self.paste)
    self.txtarea.bind("<Control-u>",self.undo)
    
# Creating TK Container
root = Tk()
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()
