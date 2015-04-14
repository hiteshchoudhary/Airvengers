#!/usr/bin/env python

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#       Thanks for opting for GUI version of AirCrack set of tools. This project is in early stage and require your support.             #
#       Project is based on Aircrack-ng set of tools and is specially designed to run on KALI LINUX.                                     #
#                                                                                                                                        #
#              Designed by : Hitesh Choudhary                                                                                            #
#              Home page   : www.HiteshChoudhary.com                                                                                     #
#              Email       : hitesh@hiteshchoudhary.com                                                                                  #
#              Based on    : www.Aircrack-ng.org                                                                                         #
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#





from Canvas import Line
from Tkinter import *
from Tkinter import Frame, PhotoImage, Text, Label, Button
from distutils.cmd import Command
import subprocess
import commands
from textwrap import fill
from tkFont import Font
import tkFont
import tkMessageBox
from ttk import Notebook
import pcapy
import sys
import tkFileDialog

class Feedback:
    
    def __init__(self, master):
	self.fname="" 
        self.t1=StringVar()
        self.t2=StringVar()
        self.t3=StringVar()
        self.t4=StringVar()
        self.var1=StringVar()
        self.var2=StringVar()
        self.var3=StringVar()
        self.var4=StringVar()
        
        mymaster = Frame(master, name='mymaster') # create Frame in "root"
        mymaster.pack(fill=BOTH)
        #min and max size of window    
        #master.minsize(width=900, height=900)
        #master.maxsize(width=550, height=350)
        #end
        
        #title of window
        master.title("Airserv-ng")
        #end
        
        #for the style of fonts
        self.customFont = tkFont.Font(family="Helvetica", size=12)
        self.myfont = tkFont.Font(family="Helvetica", size=10)
        self.myfont2 = tkFont.Font(family="Helvetica", size=8)
        self.headerfont=tkFont.Font(family="Helvetica", size=15,underline = True)
        self.myfontnew=tkFont.Font(family="Helvetica", size=11,underline = True)
        #end
        
        
       
        nb = Notebook(mymaster, name='nb') # create Notebook in "master"
        nb.pack(fill=BOTH, padx=2, pady=3) # fill "master" but pad sides
        #content frame
        self.frame_content = Frame(nb,name="frame_content", bg="white")
        self.frame_content.pack(fill=BOTH, side=TOP, expand=True)
        nb.add(self.frame_content, text="Filter-1") # add tab to Notebook
    
        # repeat for each tab
        self.frame_content7 = Frame(nb, name='frame_content7', bg="white")
        nb.add(self.frame_content7, text="Detect Devices")
        self.frame_content5 = Frame(nb, name='frame_content5', bg="white")
        nb.add(self.frame_content5, text="output")
        #End
	#frame content 7
	Label(self.frame_content7, text = 'Aigraph-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        btndetect=Button(self.frame_content7, text = 'Detect', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 1, column = 0, padx = 5, pady = 5)
		
	btndbrowse=Button(self.frame_content7, text = 'Attach File', command =self.browse_file, height=2, width=15, font=self.customFont).grid(row = 3, column = 0, padx = 5, pady = 5)	
	self.lilnew1=Listbox(self.frame_content7,bg="black", fg="white", font=self.myfont, selectmode=SINGLE, width=30, height=15)
        self.lilnew1.grid(row = 1, column = 1, rowspan=3)
	#End        

        Label(self.frame_content, text = 'Airserv-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        Label(self.frame_content, text = 'Options :',font=self.myfontnew, bg="white").grid(row = 1, column = 1)
        #Button(self.frame_content, text = 'ivs', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 2, column = 0, padx = 5, pady = 5)
        #Button(self.frame_content, text = 'gpsd', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 2, column = 1, padx = 5, pady = 5)
        #Button(self.frame_content, text = 'write', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 2, column = 2, padx = 5, pady = 5)
        #command Listbox
        Label(self.frame_content5, text = 'Edit Command From Here',font=self.myfontnew, bg="white", justify=LEFT).grid(row = 0, column = 0)
        TextCommandBox=Text(self.frame_content5, height=5, width=30)
        TextCommandBox.grid(row=1, column=0, padx=5, pady=5)
        self.output=Text(self.frame_content5,bg="black", fg="white", font=self.myfont, height=15, width=30)
        self.output.grid(row = 0, column = 1, padx=50, pady=5, rowspan=3)
        btnsubmit=Button(self.frame_content5, width=15, height=2, text="Get Result", command=self.mycallback)
        btnsubmit.grid(row=2, column=0)
        btnclear=Button(self.frame_content5, width=15, height=2, text="Clear Output", command=self.clearoutput)
        btnclear.grid(row=3, column=0)
        #end
        self.C1 = Checkbutton(self.frame_content, text = "-p", \
                 onvalue="-p",offvalue="", height=1, \
                 width = 7, bg="white", font=self.customFont, variable=self.var1)
        self.C1.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.t1=Text(self.frame_content,height=1,width = 20)
        self.t1.grid(row = 2, column = 1, padx = 5, pady = 5)
        l1=Label(self.frame_content, text = ': TCP port to listen on. Defaults to 666.',font=self.myfont, bg="white", justify=LEFT).grid(row = 2, column = 2, padx = 5, pady = 5)
        
        self.C2 = Checkbutton(self.frame_content, text = "-d", \
                 onvalue = "-d", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var2)
        self.C2.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.t2=Text(self.frame_content,height=1,width = 20)
        self.t2.grid(row = 3, column = 1, padx = 5, pady = 5)
        l2=Label(self.frame_content, text = ': wifi device to serve.',font=self.myfont, bg="white", justify=LEFT).grid(row = 3, column = 2, padx = 5, pady = 5)
        
        self.C3 = Checkbutton(self.frame_content, text = "-c", \
                 onvalue = "-c", offvalue ="", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var3)
        self.C3.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.t3=Text(self.frame_content,height=1,width = 20)
        self.t3.grid(row = 4, column = 1, padx = 5, pady = 5)
        l3=Label(self.frame_content, text = ':   Channel to start on.',font=self.myfont, bg="white", justify=LEFT).grid(row = 4, column = 2, padx = 5, pady = 5)
        
        self.C4 = Checkbutton(self.frame_content, text = "-v", \
                 onvalue = "-v", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var4)
        self.C4.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.t4=Text(self.frame_content,height=1,width = 20)
        self.t4.grid(row = 5, column = 1, padx = 5, pady = 5)
        l4=Label(self.frame_content, text = ': debug level.',font=self.myfont, bg="white", justify=LEFT).grid(row = 5, column = 2, padx = 5, pady = 5)
    
            
      
        #end    
    def mycallback(self):
         
        listselection=""
	try:
		listselection=self.lilnew1.get(self.lilnew1.curselection()[0])
	except:
		listselection=""
		
	h1="mon0"
	print listselection
	print self.fname

        listoutput=commands.getoutput("airserv-ng"+" "+format(self.var1.get())+" "+(self.t1.get(1.0, 'end')).strip()+" "+format(self.var2.get())+" "+(self.t2.get(1.0, 'end')).strip()+" "+format(self.var3.get())+" "+(self.t3.get(1.0, 'end')).strip()+" "+format(self.var4.get())+" "+(self.t4.get(1.0, 'end')).strip()+" "+listselection+" "+self.fname)
        self.output.insert(INSERT,listoutput)
    def clearoutput(self):
        self.output.delete(1.0, END)

    
    def canvas_detect(self):
        self.lilnew1.delete(0, END)
        holddevices=pcapy.findalldevs()
	for devices in holddevices:
            if devices=="any":
                self.lilnew1.insert(0, )    
	    elif devices=="lo": 
		self.lilnew1.insert(0, )      
            else:
                self.lilnew1.insert(0, devices)
    def browse_file(self):

    	self.fname = tkFileDialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
    
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    #for open the next page
def callback():
    execfile("mygui3.py")
    return
def newWindow():
    #os.startfile("mygui2.py")
    theproc = subprocess.Popen("mygui2.py", shell = True)
    theproc.communicate()   

#         end
# def openFile1(self):
#     os.startfile("mygui2.py")
    
if __name__ == "__main__": main()
