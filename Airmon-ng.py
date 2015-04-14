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
import subprocess
from textwrap import fill
from tkFont import Font
import tkFont
import tkMessageBox
from distutils.cmd import Command
import pcapy

class Feedback:
    
    def __init__(self, master):
        
        #min and max size of window    
        #master.minsize(width=410, height=680)
        #master.maxsize(width=410, height=680)
        #end
        
        #title of window
        master.title("Airmon-ng")
        #end
        
        #for the style of fonts
        self.customFont = tkFont.Font(family="Helvetica", size=15)
        self.myfont = tkFont.Font(family="Helvetica", size=12)
        self.myfont2 = tkFont.Font(family="Helvetica", size=10)
        self.headerfont=tkFont.Font(family="Helvetica", size=20)
        #end
        
        
        #content frame
        self.frame_content = Frame(master, bg="white")
        self.frame_content.pack(fill=BOTH, side=TOP, expand=True)
        Label(self.frame_content, text = 'Airmon-ng',font=self.headerfont, bg="white").grid(row = 0, column = 0)
        btndetect=Button(self.frame_content, text = 'Detect', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 1, column = 0, padx = 5, pady = 5)
        #Mycanvas=Canvas(self.frame_content, height=200, width=200, bd=2).grid(row = 1, column = 1)
        #listbox1
        lil1=Listbox(self.frame_content,bg="black", fg="white", font=self.myfont)
        lil1.grid(row = 1, column = 1)
        #end
        #listbox2
        lil2=Listbox(self.frame_content,bg="black", fg="white", font=self.myfont)
        lil2.grid(row = 3, column = 1)
        #end
        Label(self.frame_content, text = 'Kill these processes',font=self.myfont, bg="white").grid(row = 2, column = 1)
        Button(self.frame_content, text = 'Check', command =self.canvas_detect_check, height=2, width=15, font=self.customFont).grid(row = 3, column = 0, padx = 5, pady = 5)
        #canvas2=Canvas(self.frame_content, height=200, width=200, bd=2).grid(row = 3, column = 1)
        Button(self.frame_content, text = 'Kill', height=2, width=15, font=self.customFont, command=self.killprocess).grid(row = 4, column = 0, padx = 1, pady = 1)
	self.mykill=Text(self.frame_content, height=2, width=15, font=self.customFont)
	self.mykill.grid(row = 4, column = 1, padx = 1, pady = 1)
        btnstart=Button(self.frame_content, text = 'Start', command=self.item_selStart, height=2, width=15, font=self.customFont).grid(row = 5, column = 0, padx = 1, pady = 5)
        #btnstart.bind('<ListboxSelect>', self.OnDouble)
        Button(self.frame_content, text = 'Stop', height=2, width=15, font=self.customFont, command=self.item_selStop).grid(row = 5, column = 1, padx = 1, pady = 5)
        Label(self.frame_content, text = 'www.hiteshchoudhary.com',font=self.myfont, bg="white").grid(row = 6, column = 0, columnspan=2)
        self.lilnew1=Listbox(self.frame_content,bg="black", fg="white", font=self.myfont, selectmode=SINGLE)
        self.lilnew1.grid(row = 1, column = 1)
        self.lilnew2=Text(self.frame_content,bg="black", fg="white", font=self.myfont, width=20, height=12)
        self.lilnew2.grid(row = 3, column = 1)
        #End
   
    #for canvas commands loop function
    
    
    def killprocess(self):
    
        try:
            val12=self.mykill.get(1.0, 'end')
	    Detect=subprocess.call(["kill" " "+val12], shell=True)
	    print Detect
        except:
            print "please select one"   

    def item_selStart(self):
    
        try:
            val12=self.lilnew1.get(self.lilnew1.curselection()[0])
	    Detect=subprocess.check_output(["airmon-ng", "start",val12])
	    print Detect
        except:
            print "please select one"   


    def item_selStop(self):
    
        try:
            val12=self.lilnew1.get(self.lilnew1.curselection()[0])
	    Detect=subprocess.check_output(["airmon-ng", "stop",val12])
	    print Detect
        except:
            print "please select one"       

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

        
    def canvas_detect_check(self):
   	
     	Detect=subprocess.check_output(["airmon-ng", "check"])
	print Detect
	self.lilnew2.delete(1.0, END)
	self.lilnew2.insert(INSERT,Detect)

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        tkMessageBox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')
                            
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

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
