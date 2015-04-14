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
from textwrap import fill
from tkFont import Font
import tkFont
import tkMessageBox
from ttk import Notebook
import commands
import pcapy
import sys
import tkFileDialog

class Feedback:
    
    def __init__(self, master):
        
	self.fname=""
        #global variables
        self.t1=StringVar()
        self.t2=StringVar()
        self.t3=StringVar()
        self.t4=StringVar()
        self.t5=StringVar()
        self.t6=StringVar()
        self.t7=StringVar()
        self.t8=StringVar()
        self.t9=StringVar()
        self.t10=StringVar()
        self.t11=StringVar()
        self.t12=StringVar()
        self.t13=StringVar()
        self.t14=StringVar()
        self.t15=StringVar()
        self.t16=StringVar()
        self.t17=StringVar()
        self.t18=StringVar()
        self.t19=StringVar()
        self.t20=StringVar()
        self.t21=StringVar()
        self.t22=StringVar()
        self.t23=StringVar()
        self.t24=StringVar()
        self.t25=StringVar()
        self.t26=StringVar()
        
        self.var1=StringVar()
        self.var2=StringVar()
        self.var3=StringVar()
        self.var4=StringVar()
        self.var5=StringVar()
        self.var6=StringVar()
        self.var7=StringVar()
        self.var8=StringVar()
        self.var9=StringVar()
        self.var10=StringVar()
        self.var11=StringVar()
        self.var12=StringVar()
        self.var13=StringVar()
        self.var14=StringVar()
        self.var15=StringVar()
        self.var16=StringVar()
        self.var17=StringVar()
        self.var18=StringVar()
        self.var19=StringVar()
        self.var20=StringVar()
        self.var21=StringVar()
        self.var22=StringVar()
        self.var23=StringVar()
        self.var24=StringVar()
        self.var25=StringVar()
        self.var26=StringVar()
        #end
        
        mymaster = Frame(master, name='mymaster') # create Frame in "root"
        mymaster.pack(fill=BOTH)
        #min and max size of window    
        #master.minsize(width=900, height=900)
        #master.maxsize(width=650, height=410)
        #end
        
        #title of window
        master.title("Airodump-ng")
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
        self.frame_content2 = Frame(nb, name='frame_content2', bg="white")
        nb.add(self.frame_content2, text="Filter-2")
        self.frame_content3 = Frame(nb, name='frame_content3', bg="white")
        nb.add(self.frame_content3, text="Filter-3")
        self.frame_content4 = Frame(nb, name='frame_content4', bg="white")
        nb.add(self.frame_content4, text="Filter-4")
	self.frame_content7 = Frame(nb, name='frame_content7', bg="white")
        nb.add(self.frame_content7, text="Detect Devices")        
	self.frame_content5 = Frame(nb, name='frame_content5', bg="white")
        nb.add(self.frame_content5, text="output")
        #End
        
	#frame content 7
	Label(self.frame_content7, text = 'Airodump-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        btndetect=Button(self.frame_content7, text = 'Detect', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 1, column = 0, padx = 5, pady = 5)
		
	btndbrowse=Button(self.frame_content7, text = 'Attach File', command =self.browse_file, height=2, width=15, font=self.customFont).grid(row = 3, column = 0, padx = 5, pady = 5)	
	self.lilnew1=Listbox(self.frame_content7,bg="black", fg="white", font=self.myfont, selectmode=SINGLE, width=30, height=15)
        self.lilnew1.grid(row = 1, column = 1, rowspan=3)
	#End

        Label(self.frame_content, text = 'Airodump-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        Label(self.frame_content, text = 'Options :',font=self.myfontnew, bg="white").grid(row = 1, column = 1)
        #Button(self.frame_content, text = 'ivs', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 2, column = 0, padx = 5, pady = 5)
        #Button(self.frame_content, text = 'gpsd', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 2, column = 1, padx = 5, pady = 5)
        #Button(self.frame_content, text = 'write', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 2, column = 2, padx = 5, pady = 5)
        #command Listbox
        Label(self.frame_content5, text = 'Edit Command From Here',font=self.myfontnew, bg="white", justify=LEFT).grid(row = 0, column = 0)
        TextCommandBox=Text(self.frame_content5, height=5, width=30)
        TextCommandBox.grid(row=1, column=0, padx=5, pady=5)
        self.output=Text(self.frame_content5,bg="black", fg="white", font=self.myfont, height=20, width=42)
        self.output.grid(row = 0, column = 1, padx=50, pady=5, rowspan=3)
        btnsubmit=Button(self.frame_content5, width=15, height=2, text="Get Result", command=self.mycallback)
        btnsubmit.grid(row=2, column=0)
        btnclear=Button(self.frame_content5, width=15, height=2, text="Clear Output", command=self.clearoutput)
        btnclear.grid(row=3, column=0)
        #end
        self.C1 = Checkbutton(self.frame_content, text = "--ivs", \
                 onvalue = "--ivs", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var1)
        self.C1.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.t1=Text(self.frame_content,height=1,width = 20)
        self.t1.grid(row = 2, column = 1, padx = 5, pady = 5)
        l1=Label(self.frame_content, text = ': Save only captured IVs',font=self.myfont, bg="white", justify=LEFT).grid(row = 2, column = 2, padx = 5, pady = 5)
        
        self.C2 = Checkbutton(self.frame_content, text = "--gpsd", \
                 onvalue = "--gpsd", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var2)
        self.C2.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.t2=Text(self.frame_content,height=1,width = 20)
        self.t2.grid(row = 3, column = 1, padx = 5, pady = 5)
        l2=Label(self.frame_content, text = ': Use GPSd',font=self.myfont, bg="white", justify=LEFT).grid(row = 3, column = 2, padx = 5, pady = 5)
        
        self.C3 = Checkbutton(self.frame_content, text = "--write", \
                 onvalue = "--write", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var3)
        self.C3.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.t3=Text(self.frame_content,height=1,width = 20)
        self.t3.grid(row = 4, column = 1, padx = 5, pady = 5)
        l3=Label(self.frame_content, text = ': Dump file prefix',font=self.myfont, bg="white", justify=LEFT).grid(row = 4, column = 2, padx = 5, pady = 5)
        
        self.C4 = Checkbutton(self.frame_content, text = "-w", \
                 onvalue = "-w", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var4)
        self.C4.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.t4=Text(self.frame_content,height=1,width = 20)
        self.t4.grid(row = 5, column = 1, padx = 5, pady = 5)
        l4=Label(self.frame_content, text = ': same as --write',font=self.myfont, bg="white", justify=LEFT).grid(row = 5, column = 2, padx = 5, pady = 5)
        
        self.C5 = Checkbutton(self.frame_content, text = "--beacons", \
                 onvalue = "--beacon", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var5)
        self.C5.grid(row = 6, column = 0, padx = 5, pady = 5)
        self.t5=Text(self.frame_content,height=1,width = 20)
        self.t5.grid(row = 6, column = 1, padx = 5, pady = 5)
        l5=Label(self.frame_content, text = ': Record all beacons in dump file',font=self.myfont, bg="white", justify=LEFT).grid(row = 6, column = 2, padx = 5, pady = 5)
        
        self.C6 = Checkbutton(self.frame_content, text = "--update", \
                 onvalue = "--update", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var6)
        self.C6.grid(row = 7, column = 0, padx = 5, pady = 5)
        self.t6=Text(self.frame_content,height=1,width = 20)
        self.t6.grid(row = 7, column = 1, padx = 5, pady = 5)
        l6=Label(self.frame_content, text = ': Display update delay in seconds',font=self.myfont, bg="white", justify=LEFT).grid(row = 7, column = 2, padx = 5, pady = 5)
        
        self.C7 = Checkbutton(self.frame_content, text = "--showack", \
                 onvalue = "--showack", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var7)
        self.C7.grid(row = 8, column = 0, padx = 5, pady = 5)
        self.t7=Text(self.frame_content,height=1,width = 20)
        self.t7.grid(row = 8, column = 1, padx = 5, pady = 5)
        l7=Label(self.frame_content, text = ': Prints ack/cts/rts statistics',font=self.myfont, bg="white", justify=LEFT).grid(row = 8, column = 2, padx = 5, pady = 5)
        
        self.C8 = Checkbutton(self.frame_content2, text = "-h", \
                 onvalue = "-h", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var8)
        self.C8.grid(row = 9, column = 0, padx = 5, pady = 5)
        self.t8=Text(self.frame_content2,height=1,width = 20)
        self.t8.grid(row = 9, column = 1, padx = 5, pady = 5)
        l8=Label(self.frame_content2, text = ': Hides known stations for --showack',font=self.myfont, bg="white", justify=LEFT).grid(row = 9, column = 2, padx = 5, pady = 5)
        
        self.C9 = Checkbutton(self.frame_content2, text = "-f", \
                 onvalue = "-f", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var9)
        self.C9.grid(row = 10, column = 0, padx = 5, pady = 5)
        self.t9=Text(self.frame_content2,height=1,width = 20)
        self.t9.grid(row = 10, column = 1, padx = 5, pady = 5)
        l9=Label(self.frame_content2, text = ': Time in ms between hopping channels',font=self.myfont, bg="white", justify=LEFT).grid(row = 10, column = 2, padx = 5, pady = 5)
        
        Label(self.frame_content2, text = 'Airodump-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        
        self.C10 = Checkbutton(self.frame_content2, text = "--berlin", \
                 onvalue = "--berlin", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var10)
        self.C10.grid(row = 11, column = 0, padx = 5, pady = 5)
        self.t10=Text(self.frame_content2,height=1,width = 20)
        self.t10.grid(row = 11, column = 1, padx = 5, pady = 5)
        l10=Label(self.frame_content2, text = ': Time before removing the AP/client',font=self.myfont, bg="white", justify=LEFT).grid(row = 11, column = 2, padx = 5, pady = 5)
        
        self.C11 = Checkbutton(self.frame_content2, text = "-r", \
                 onvalue = "-r", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var11)
        self.C11.grid(row = 12, column = 0, padx = 5, pady = 5)
        self.t11=Text(self.frame_content2,height=1,width = 20)
        self.t11.grid(row = 12, column = 1, padx = 5, pady = 5)
        l11=Label(self.frame_content2, text = ': Read packets from that file',font=self.myfont, bg="white", justify=LEFT).grid(row = 12, column = 2, padx = 5, pady = 5)
        
        self.C12 = Checkbutton(self.frame_content2, text = "-x", \
                 onvalue = "-x", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var12)
        self.C12.grid(row = 13, column = 0, padx = 5, pady = 5)
        self.t12=Text(self.frame_content2,height=1,width = 20)
        self.t12.grid(row = 13, column = 1, padx = 5, pady = 5)
        l12=Label(self.frame_content2, text = ': Active Scanning Simulation',font=self.myfont, bg="white", justify=LEFT).grid(row = 13, column = 2, padx = 5, pady = 5)
        
        self.C13 = Checkbutton(self.frame_content2, text = " --output-format", \
                 onvalue = "--output-format", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var13)
        self.C13.grid(row = 14, column = 0, padx = 5, pady = 5)
        self.t13=Text(self.frame_content2,height=1,width = 20)
        self.t13.grid(row = 14, column = 1, padx = 5, pady = 5)
        l13=Label(self.frame_content2, text = ': Output format. Possible values',font=self.myfont, bg="white", justify=LEFT).grid(row = 14, column = 2, padx = 5, pady = 5)
        
        self.C14 = Checkbutton(self.frame_content2, text = " --ignore-negative-one", \
                 onvalue = "--ignore-negative-one", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var14)
        self.C14.grid(row = 15, column = 0, padx = 5, pady = 5)
        self.t14=Text(self.frame_content2,height=1,width = 20)
        self.t14.grid(row = 15, column = 1, padx = 5, pady = 5)
        l14=Label(self.frame_content2, text = ': Removes the message that says fixed channel',font=self.myfont, bg="white").grid(row = 15, column = 2, padx = 5, pady = 5)
        
        
        Label(self.frame_content3, text = 'Airodump-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        Label(self.frame_content3, text = 'Filter Options :',font=self.myfontnew, bg="white", justify=LEFT).grid(row = 16, column = 1)
        
        self.C15 = Checkbutton(self.frame_content3, text = "--encrypt", \
                 onvalue = "--encrypt", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var15)
        self.C15.grid(row = 17, column = 0, padx = 5, pady = 5)
        self.t15=Text(self.frame_content3,height=1,width = 20)
        self.t15.grid(row = 17, column = 1, padx = 5, pady = 5)
        l15=Label(self.frame_content3, text = ': Filter APs by cipher suite',font=self.myfont, bg="white", justify=LEFT).grid(row = 17, column = 2, padx = 5, pady = 5)
        
        self.C16 = Checkbutton(self.frame_content3, text = "--netmask", \
                 onvalue = "--netmask", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var16)
        self.C16.grid(row = 18, column = 0, padx = 5, pady = 5)
        self.t16=Text(self.frame_content3,height=1,width = 20)
        self.t16.grid(row = 18, column = 1, padx = 5, pady = 5)
        l16=Label(self.frame_content3, text = ': Filter APs by mask',font=self.myfont, bg="white", justify=LEFT).grid(row = 18, column = 2, padx = 5, pady = 5)
        
        self.C17 = Checkbutton(self.frame_content3, text = "--bssid", \
                 onvalue = "--bssid", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var17)
        self.C17.grid(row = 19, column = 0, padx = 5, pady = 5)
        self.t17=Text(self.frame_content3,height=1,width = 20)
        self.t17.grid(row = 19, column = 1, padx = 5, pady = 5)
        l17=Label(self.frame_content3, text = ': Filter APs by BSSID',font=self.myfont, bg="white", justify=LEFT).grid(row = 19, column = 2, padx = 5, pady = 5)
        
        self.C18 = Checkbutton(self.frame_content3, text = "--essid", \
                 onvalue = "--essid", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var18)
        self.C18.grid(row = 20, column = 0, padx = 5, pady = 5)
        self.t18=Text(self.frame_content3,height=1,width = 20)
        self.t18.grid(row = 20, column = 1, padx = 5, pady = 5)
        l18=Label(self.frame_content3, text = ': Filter APs by ESSID',font=self.myfont, bg="white", justify=LEFT).grid(row = 20, column = 2, padx = 5, pady = 5)
        
        self.C19 = Checkbutton(self.frame_content3, text = "--essid-regex", \
                 onvalue = "--essid-regex", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var19)
        self.C19.grid(row = 21, column = 0, padx = 5, pady = 5)
        self.t19=Text(self.frame_content3,height=1,width = 20)
        self.t19.grid(row = 21, column = 1, padx = 5, pady = 5)
        l19=Label(self.frame_content3, text = ': Filter APs by ESSID using \n  a regular expression',font=self.myfont, bg="white", justify=LEFT).grid(row = 21, column = 2, padx = 5, pady = 5)
        
        self.C20 = Checkbutton(self.frame_content3, text = "-a", \
                 onvalue = "-a", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var20)
        self.C20.grid(row = 22, column = 0, padx = 5, pady = 5)
        self.t20=Text(self.frame_content3,height=1,width = 20)
        self.t20.grid(row = 22, column = 1, padx = 5, pady = 5)
        l20=Label(self.frame_content3, text = ': Filter unassociated clients',font=self.myfont, bg="white", justify=LEFT).grid(row = 22, column = 2, padx = 5, pady = 5)
        
        Label(self.frame_content4, text = 'Airodump-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        
        self.C21 = Checkbutton(self.frame_content4, text = "--channel", \
                 onvalue = "--channel", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var21)
        self.C21.grid(row = 23, column = 0, padx = 5, pady = 5)
        self.t21=Text(self.frame_content4,height=1,width = 20)
        self.t21.grid(row = 23, column = 1, padx = 5, pady = 5)
        l21=Label(self.frame_content4, text = ': Capture on specific channels',font=self.myfont, bg="white", justify=LEFT).grid(row = 23, column = 2, padx = 5, pady = 5)
        
        self.C22 = Checkbutton(self.frame_content4, text = "--band", \
                 onvalue = "--band", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var22)
        self.C22.grid(row = 24, column = 0, padx = 5, pady = 5)
        self.t22=Text(self.frame_content4,height=1,width = 20)
        self.t22.grid(row = 24, column = 1, padx = 5, pady = 5)
        l22=Label(self.frame_content4, text = ':  Band on which airodump-ng should hop',font=self.myfont, bg="white", justify=LEFT).grid(row = 24, column = 2, padx = 5, pady = 5)
        
        self.C23 = Checkbutton(self.frame_content4, text = "-C", \
                 onvalue = "-C", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var23)
        self.C23.grid(row = 25, column = 0, padx = 5, pady = 5)
        self.t23=Text(self.frame_content4,height=1,width = 20)
        self.t23.grid(row = 25, column = 1, padx = 5, pady = 5)
        l23=Label(self.frame_content4, text = ':  Uses these frequencies in MHz to hop',font=self.myfont, bg="white", justify=LEFT).grid(row = 25, column = 2, padx = 5, pady = 5)
        
        self.C24 = Checkbutton(self.frame_content4, text = "-s", \
                 onvalue = "-s", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var24)
        self.C24.grid(row = 26, column = 0, padx = 5, pady = 5)
        self.t24=Text(self.frame_content4,height=1,width = 20)
        self.t24.grid(row = 26, column = 1, padx = 5, pady = 5)
        l24=Label(self.frame_content4, text = ':  same as --cswitch',font=self.myfont, bg="white", justify=LEFT).grid(row = 26, column = 2, padx = 5, pady = 5)
        
        self.C25 = Checkbutton(self.frame_content3, text = "--cswitch", \
                 onvalue = "--cswitch", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var25)
        self.C25.grid(row = 27, column = 0, padx = 5, pady = 5)
        self.t25=Text(self.frame_content3,height=1,width = 20)
        self.t25.grid(row = 27, column = 1, padx = 5, pady = 5)
        l25=Label(self.frame_content3, text = ':  Set channel switching method',font=self.myfont, bg="white", justify=LEFT).grid(row = 27, column = 2, padx = 5, pady = 5)
        
        self.C26 = Checkbutton(self.frame_content4, text = "--help", \
                 onvalue = "--help", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var26)
        self.C26.grid(row = 28, column = 0, padx = 5, pady = 5)
        self.t26=Text(self.frame_content4,height=1,width = 20)
        self.t26.grid(row = 28, column = 1, padx = 5, pady = 5)
        l26=Label(self.frame_content4, text = ':  Displays this usage screen',font=self.myfont, bg="white", justify=LEFT).grid(row = 28, column = 2, padx = 5, pady = 5)
        
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
         
        listoutput=commands.getoutput("airodump-ng"+" "+format(self.var1.get())+" "+(self.t1.get(1.0, 'end')).strip()+" "+format(self.var2.get())+" "+(self.t2.get(1.0, 'end')).strip()+" "+format(self.var3.get())+" "+(self.t3.get(1.0, 'end')).strip()+" "+format(self.var4.get())+" "+(self.t4.get(1.0, 'end')).strip()+" "+\
                            format(self.var5.get())+" "+(self.t5.get(1.0, 'end')).strip()+" "+format(self.var6.get())+" "+(self.t6.get(1.0, 'end')).strip()+" "+format(self.var7.get())+" "+(self.t7.get(1.0, 'end')).strip()+" "+format(self.var8.get())+" "+(self.t8.get(1.0, 'end')).strip()+" "+\
                            format(self.var9.get())+" "+(self.t9.get(1.0, 'end')).strip()+" "+format(self.var10.get())+" "+(self.t10.get(1.0, 'end')).strip()+" "+format(self.var11.get())+" "+(self.t11.get(1.0, 'end')).strip()+" "+format(self.var12.get())+" "+(self.t12.get(1.0, 'end')).strip()+" "+\
                            format(self.var13.get())+" "+(self.t13.get(1.0, 'end')).strip()+" "+format(self.var14.get())+" "+(self.t14.get(1.0, 'end')).strip()+" "+format(self.var15.get())+" "+(self.t15.get(1.0, 'end')).strip()+" "+format(self.var16.get())+" "+(self.t16.get(1.0, 'end')).strip()+" "+\
                            format(self.var17.get())+" "+(self.t17.get(1.0, 'end')).strip()+" "+format(self.var18.get())+" "+(self.t18.get(1.0, 'end')).strip()+" "+format(self.var19.get())+" "+(self.t19.get(1.0, 'end')).strip()+" "+format(self.var20.get())+" "+(self.t20.get(1.0, 'end')).strip()+" "+\
                            format(self.var21.get())+" "+ (self.t21.get(1.0, 'end')).strip()+" "+format(self.var22.get())+" "+(self.t22.get(1.0, 'end')).strip()+" "+format(self.var23.get())+" "+(self.t23.get(1.0, 'end')).strip()+" "+format(self.var24.get())+" "+(self.t24.get(1.0, 'end')).strip()+" "+\
                            format(self.var25.get())+" "+(self.t25.get(1.0, 'end')).strip()+" "+format(self.var26.get())+" "+(self.t26.get(1.0, 'end')).strip()+" "+listselection+" "+self.fname)
       
      
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
