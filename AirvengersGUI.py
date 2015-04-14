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

class Feedback:
    
    def __init__(self, master):
        
        #min and max size of window    
        #master.minsize(width=410, height=700)
        #master.maxsize(width=410, height=700)
        #end
        
        #title of window
        master.title("Airvengers")
        #end
        
        #for scrolling the page
       
        
       
        #end
        
        #for the style of fonts
        self.customFont = tkFont.Font(family="Helvetica", size=15)
        self.myfont = tkFont.Font(family="Helvetica", size=12)
        self.myfont2 = tkFont.Font(family="Helvetica", size=10)
        #end
       
        
        #header frame
        self.frame_header = Frame(master, bg="white")
        self.frame_header.pack(fill=BOTH, side=TOP, expand=True)
        self.logo = PhotoImage(file = "logoair.gif")
        Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, sticky='sw', columnspan=2)
        #end
        
        #content frame
        self.frame_content = Frame(master, bg="white")
        self.frame_content.pack(fill=BOTH, side=TOP, expand=True)
       
        Label(self.frame_content, text = 'Based on:' ,font=self.myfont, wraplength =200, bg="white").grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        Label(self.frame_content, text = 'GUI by Hitesh:', font=self.myfont, wraplength =200,padx=0, bg="white").grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        Label(self.frame_content, text = 'Aircrack-ng' ,font=self.myfont, wraplength =300, bg="white").grid(row = 1, column = 0, padx = 5, sticky = 'sw')
        Label(self.frame_content, text = 'hitesh@hiteshchoudhary.com', font=self.myfont2, wraplength =300,padx=0, bg="white").grid(row = 1, column = 1, padx = 5, sticky = 'sw')
        
        #Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        #self.entry_name = Entry(self.frame_content, width = 24)
        #self.entry_email = Entry(self.frame_content, width = 24)
        #self.text_comments = Text(self.frame_content, width = 50, height = 10)

        #self.entry_name.grid(row = 1, column = 0, padx = 5)
        #self.entry_email.grid(row = 1, column = 1, padx = 5)
        #self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
        
        

        Button(self.frame_content, text = 'airmon-ng', command =AirmonNg, height=2, width=15, font=self.customFont).grid(row = 4, column = 0, padx = 5, pady = 5)
        Button(self.frame_content, text = 'aircrack-ng', command=AircrackNg,  height=2, width=15, font=self.customFont).grid(row = 4, column = 1, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airdecap-ng' , command = AirdecapNg,  height=2, width=15, font=self.customFont).grid(row = 5, column = 0, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airdecloak-ng', command = AirdecloakNg,  height=2, width=15, font=self.customFont).grid(row = 5, column = 1, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airdrop-ng', command = AirdropNg,  height=2, width=15, font=self.customFont).grid(row = 6, column = 0, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'aireplay-ng', command = AireplayNg,  height=2, width=15, font=self.customFont).grid(row = 6, column = 1, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airgraph-ng', command = AirgraphNg,  height=2, width=15, font=self.customFont).grid(row = 7, column = 0, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airbase-ng', command = AirbaseNg,  height=2, width=15, font=self.customFont).grid(row = 7, column = 1, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airodump-ng', command = AirodumpNg,  height=2, width=15, font=self.customFont).grid(row = 8, column = 0, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airolib-ng', command = AirolibNg,  height=2, width=15, font=self.customFont).grid(row = 8, column = 1, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airserv-ng ', command = AirservNg,  height=2, width=15, font=self.customFont).grid(row = 9, column = 0, padx = 5, pady = 5 )
        Button(self.frame_content, text = 'airtun-ng ', command = AirtunNg,  height=2, width=15, font=self.customFont).grid(row = 9, column = 1, padx = 5, pady = 5)
        
                            
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
def AirmonNg():
    
    subprocess.call(["python","Airmon-ng.py"])
    
def AirodumpNg():
    
    subprocess.call(["python","Airodump-ng.py"])
    
def AirbaseNg():
    
    subprocess.call(["python","Airbase-ng.py"])   

def AircrackNg():
    
    subprocess.call(["python","Aircrack-ng.py"]) 
    
def AirdecapNg():
    
    subprocess.call(["python","Airdecap-ng.py"]) 
    
def AirdecloakNg():
    
    subprocess.call(["python","Airdecloak-ng.py"]) 
    
def AirdropNg():
    
    subprocess.call(["python","Airdrop-ng.py"]) 
    
def AireplayNg():
    
    subprocess.call(["python","Aireplay-ng.py"]) 
    
def AirgraphNg():
    
    subprocess.call(["python","Aigraph-ng.py"]) 
    
def AirolibNg():
    
    subprocess.call(["python","Airolib-ng.py"]) 
    
def AirservNg():
    
    subprocess.call(["python","Airserv-ng.py"]) 
    
def AirtunNg():
    
    subprocess.call(["python","Airtun-ng.py"]) 
#         end
# def openFile1(self):
#     os.startfile("mygui2.py")
    
if __name__ == "__main__": main()
