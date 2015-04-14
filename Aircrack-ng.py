#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        self.t27=StringVar()
        self.t28=StringVar()
        self.t29=StringVar()
        self.t30=StringVar()
        self.t31=StringVar()
        self.t32=StringVar()
        self.t33=StringVar()
        self.t34=StringVar()
        
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
        self.var27=StringVar()
        self.var28=StringVar()
        self.var29=StringVar()
        self.var30=StringVar()
        self.var31=StringVar()
        self.var32=StringVar()
        self.var33=StringVar()
        self.var34=StringVar()
        #end
        
        mymaster = Frame(master, name='mymaster') # create Frame in "root"
        mymaster.pack(fill=BOTH)
        #min and max size of window    
        #master.minsize(width=900, height=900)
        #master.maxsize(width=750, height=470)
        #end
        
        #title of window
        master.title("Aircrack-ng")
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
        self.frame_content6 = Frame(nb, name='frame_content6', bg="white")
        nb.add(self.frame_content6, text="Filter-5")
	self.frame_content7 = Frame(nb, name='frame_content7', bg="white")
        nb.add(self.frame_content7, text="Detect Devices")
        self.frame_content5 = Frame(nb, name='frame_content5', bg="white")
        nb.add(self.frame_content5, text="output")
        
        #End
        
	#frame content 7
	Label(self.frame_content7, text = 'Aircrack-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        btndetect=Button(self.frame_content7, text = 'Detect', command =self.canvas_detect, height=2, width=15, font=self.customFont).grid(row = 1, column = 0, padx = 5, pady = 5)
		
	btndbrowse=Button(self.frame_content7, text = 'Attach File', command =self.browse_file, height=2, width=15, font=self.customFont).grid(row = 3, column = 0, padx = 5, pady = 5)	
	self.lilnew1=Listbox(self.frame_content7,bg="black", fg="white", font=self.myfont, selectmode=SINGLE, width=30, height=15)
        self.lilnew1.grid(row = 1, column = 1, rowspan=3)
	#End

        Label(self.frame_content, text = 'Aircrack-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
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
        self.C1 = Checkbutton(self.frame_content, text = "-a", \
                 onvalue = "-a", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var1)
        self.C1.grid(row = 2, column = 0, padx = 5, pady = 5)
        self.t1=Text(self.frame_content,height=1,width = 20)
        self.t1.grid(row = 2, column = 1, padx = 5, pady = 5)
        l1=Label(self.frame_content, text = ': Force attack mode (1 = static WEP, 2 = WPA/WPA2-PSK).',font=self.myfont, bg="white", justify=LEFT).grid(row = 2, column = 2, padx = 5, pady = 5)
        
        self.C2 = Checkbutton(self.frame_content, text = "-b", \
                 onvalue = "-b", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var2)
        self.C2.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.t2=Text(self.frame_content,height=1,width = 20)
        self.t2.grid(row = 3, column = 1, padx = 5, pady = 5)
        l2=Label(self.frame_content, text = ': Long version bssid. Select the target network based on\n  the access point\'s MAC address.',font=self.myfont, bg="white", justify=LEFT).grid(row = 3, column = 2, padx = 5, pady = 5)
        
        self.C3 = Checkbutton(self.frame_content, text = "-e", \
                 onvalue = "-e", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var3)
        self.C3.grid(row = 4, column = 0, padx = 5, pady = 5)
        self.t3=Text(self.frame_content,height=1,width = 20)
        self.t3.grid(row = 4, column = 1, padx = 5, pady = 5)
        l3=Label(self.frame_content, text = ': If set, all IVs from networks with the same ESSID will be used.\n  This option is also required for WPA/WPA2-PSK cracking if the\n  ESSID is not broadcasted (hidden).',font=self.myfont, bg="white", justify=LEFT).grid(row = 4, column = 2, padx = 5, pady = 5)
        
        self.C4 = Checkbutton(self.frame_content, text = "-p", \
                 onvalue = "-p", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var4)
        self.C4.grid(row = 5, column = 0, padx = 5, pady = 5)
        self.t4=Text(self.frame_content,height=1,width = 20)
        self.t4.grid(row = 5, column = 1, padx = 5, pady = 5)
        l4=Label(self.frame_content, text = ': On SMP systems: # of CPU to use. This option is invalid on\n  non-SMP systems.',font=self.myfont, bg="white", justify=LEFT).grid(row = 5, column = 2, padx = 5, pady = 5)
        
        self.C5 = Checkbutton(self.frame_content, text = "-q", \
                 onvalue = "-q", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var5)
        self.C5.grid(row = 6, column = 0, padx = 5, pady = 5)
        self.t5=Text(self.frame_content,height=1,width = 20)
        self.t5.grid(row = 6, column = 1, padx = 5, pady = 5)
        l5=Label(self.frame_content, text = ': Enable quiet mode (no status output until the key is found, or not).',font=self.myfont, bg="white", justify=LEFT).grid(row = 6, column = 2, padx = 5, pady = 5)
        
        self.C6 = Checkbutton(self.frame_content, text = "-c", \
                 onvalue = "-c", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var6)
        self.C6.grid(row = 7, column = 0, padx = 5, pady = 5)
        self.t6=Text(self.frame_content,height=1,width = 20)
        self.t6.grid(row = 7, column = 1, padx = 5, pady = 5)
        l6=Label(self.frame_content, text = ': (WEP cracking) Restrict the search space to alpha-numeric\n  characters only (0x20 - 0x7F).',font=self.myfont, bg="white", justify=LEFT).grid(row = 7, column = 2, padx = 5, pady = 5)
        
        self.C7 = Checkbutton(self.frame_content, text = "-t", \
                 onvalue = "-t", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var7)
        self.C7.grid(row = 8, column = 0, padx = 5, pady = 5)
        self.t7=Text(self.frame_content,height=1,width = 20)
        self.t7.grid(row = 8, column = 1, padx = 5, pady = 5)
        l7=Label(self.frame_content, text = ': (WEP cracking) Restrict the search space to binary coded decimal\n  hex characters.',font=self.myfont, bg="white", justify=LEFT).grid(row = 8, column = 2, padx = 5, pady = 5)
        
        Label(self.frame_content2, text = 'Aircrack-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        #frame2
        self.C8 = Checkbutton(self.frame_content2, text = "-h", \
                 onvalue = "-h", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var8)
        self.C8.grid(row = 9, column = 0, padx = 5, pady = 5)
        self.t8=Text(self.frame_content2,height=1,width = 20)
        self.t8.grid(row = 9, column = 1, padx = 5, pady = 5)
        l8=Label(self.frame_content2, text = ':  (WEP cracking) Restrict the search space to numeric\n   characters (0x30-0x39) These keys are used by default\n   in most Fritz!BOXes.',font=self.myfont, bg="white", justify=LEFT).grid(row = 9, column = 2, padx = 5, pady = 5)
        
        self.C9 = Checkbutton(self.frame_content2, text = "-d", \
                 onvalue = "-d", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var9)
        self.C9.grid(row = 10, column = 0, padx = 5, pady = 5)
        self.t9=Text(self.frame_content2,height=1,width = 20)
        self.t9.grid(row = 10, column = 1, padx = 5, pady = 5)
        l9=Label(self.frame_content2, text = ': (WEP cracking) Long version debug. Set the beginning\n  of the WEP key (in hex), for debugging purposes.',font=self.myfont, bg="white", justify=LEFT).grid(row = 10, column = 2, padx = 5, pady = 5)
        
        
        self.C10 = Checkbutton(self.frame_content2, text = "-m", \
                 onvalue = "-m", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var10)
        self.C10.grid(row = 11, column = 0, padx = 5, pady = 5)
        self.t10=Text(self.frame_content2,height=1,width = 20)
        self.t10.grid(row = 11, column = 1, padx = 5, pady = 5)
        l10=Label(self.frame_content2, text = ': (WEP cracking) MAC address to filter WEP data packets.\n  Alternatively, specify -m ff:ff:ff:ff:ff:ff to use all and every IVs,\n  regardless of the network.',font=self.myfont, bg="white", justify=LEFT).grid(row = 11, column = 2, padx = 5, pady = 5)
        
        self.C11 = Checkbutton(self.frame_content2, text = "-M", \
                 onvalue = "-M", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var11)
        self.C11.grid(row = 12, column = 0, padx = 5, pady = 5)
        self.t11=Text(self.frame_content2,height=1,width = 20)
        self.t11.grid(row = 12, column = 1, padx = 5, pady = 5)
        l11=Label(self.frame_content2, text = ': (WEP cracking) Sets the maximum number of ivs to use.',font=self.myfont, bg="white", justify=LEFT).grid(row = 12, column = 2, padx = 5, pady = 5)
        
        self.C12 = Checkbutton(self.frame_content2, text = "-n", \
                 onvalue = "-n", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var12)
        self.C12.grid(row = 13, column = 0, padx = 5, pady = 5)
        self.t12=Text(self.frame_content2,height=1,width = 20)
        self.t12.grid(row = 13, column = 1, padx = 5, pady = 5)
        l12=Label(self.frame_content2, text = ': (WEP cracking) Specify the length of the key: 64 for 40-bit\n  WEP, 128 for 104-bit WEP, etc. The default value is 128.',font=self.myfont, bg="white", justify=LEFT).grid(row = 13, column = 2, padx = 5, pady = 5)
        
        self.C13 = Checkbutton(self.frame_content2, text = "-i", \
                 onvalue = "-i", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var13)
        self.C13.grid(row = 14, column = 0, padx = 5, pady = 5)
        self.t13=Text(self.frame_content2,height=1,width = 20)
        self.t13.grid(row = 14, column = 1, padx = 5, pady = 5)
        l13=Label(self.frame_content2, text = ': (WEP cracking) Only keep the IVs that have this key index\n  (1 to 4). The default behaviour is to ignore the key index.',font=self.myfont, bg="white", justify=LEFT).grid(row = 14, column = 2, padx = 5, pady = 5)
        
        self.C14 = Checkbutton(self.frame_content2, text = "-f", \
                 onvalue = "-f", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var14)
        self.C14.grid(row = 15, column = 0, padx = 5, pady = 5)
        self.t14=Text(self.frame_content2,height=1,width = 20)
        self.t14.grid(row = 15, column = 1, padx = 5, pady = 5)
        l14=Label(self.frame_content2, text = ': (WEP cracking) By default, this parameter is set to 2 for\n  104-bit WEP and to 5 for 40-bit WEP. Specify a higher\n  value to increase the bruteforce level: cracking will take\n  more time, but with a higher likelyhood of success.',font=self.myfont, bg="white", justify=LEFT).grid(row = 15, column = 2, padx = 5, pady = 5)
        
        
        #frame3
        Label(self.frame_content3, text = 'Aircrack-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        
        self.C15 = Checkbutton(self.frame_content3, text = "-H", \
                 onvalue = "-H", offvalue = "", height=1, \
                 width = 7, bg="white", font=self.customFont,variable=self.var15)
        self.C15.grid(row = 17, column = 0, padx = 5, pady = 5)
        self.t15=Text(self.frame_content3,height=1,width = 20)
        self.t15.grid(row = 17, column = 1, padx = 5, pady = 5)
        l15=Label(self.frame_content3, text = ': Long version help. Output help information.',font=self.myfont, bg="white", justify=LEFT).grid(row = 17, column = 2, padx = 5, pady = 5)
        
        self.C16 = Checkbutton(self.frame_content3, text = "-l", \
                 onvalue = "-l", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var16)
        self.C16.grid(row = 18, column = 0, padx = 5, pady = 5)
        self.t16=Text(self.frame_content3,height=1,width = 20)
        self.t16.grid(row = 18, column = 1, padx = 5, pady = 5)
        l16=Label(self.frame_content3, text = ': (Lowercase L, ell) logs the key to the file specified.',font=self.myfont, bg="white", justify=LEFT).grid(row = 18, column = 2, padx = 5, pady = 5)
        
        self.C17 = Checkbutton(self.frame_content3, text = "-K", \
                 onvalue = "-K", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var17)
        self.C17.grid(row = 19, column = 0, padx = 5, pady = 5)
        self.t17=Text(self.frame_content3,height=1,width = 20)
        self.t17.grid(row = 19, column = 1, padx = 5, pady = 5)
        l17=Label(self.frame_content3, text = ':  (WEP cracking) There are 17 korek statistical attacks.\n   Sometimes one attack creates a huge false positive that\n   prevents the key from being found, even with lots of IVs.\n   Try -k 1, -k 2, -k 17 to disable each attack selectively.',font=self.myfont, bg="white", justify=LEFT).grid(row = 19, column = 2, padx = 5, pady = 5)
    
        
        self.C18 = Checkbutton(self.frame_content3, text = "-k", \
                 onvalue = "-k", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var18)
        self.C18.grid(row = 21, column = 0, padx = 5, pady = 5)
        self.t18=Text(self.frame_content3,height=1,width = 20)
        self.t18.grid(row = 21, column = 1, padx = 5, pady = 5)
        l18=Label(self.frame_content3, text = ': number of packets per second (default: 100)',font=self.myfont, bg="white", justify=LEFT).grid(row = 21, column = 2, padx = 5, pady = 5)
        
        self.C19 = Checkbutton(self.frame_content3, text = "-p", \
                 onvalue = "-p", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var19)
        self.C19.grid(row = 22, column = 0, padx = 5, pady = 5)
        self.t19=Text(self.frame_content3,height=1,width = 20)
        self.t19.grid(row = 22, column = 1, padx = 5, pady = 5)
        l19=Label(self.frame_content3, text = ': Allow the number of threads for cracking even if you have\n   a non-SMP computer.',font=self.myfont, bg="white", justify=LEFT).grid(row = 22, column = 2, padx = 5, pady = 5)
        
        
        self.C20 = Checkbutton(self.frame_content3, text = "-r", \
                 onvalue = "-r", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var20)
        self.C20.grid(row = 23, column = 0, padx = 5, pady = 5)
        self.t20=Text(self.frame_content3,height=1,width = 20)
        self.t20.grid(row = 23, column = 1, padx = 5, pady = 5)
        l20=Label(self.frame_content3, text = ': Utilizes a database generated by airolib-ng as input to\n   determine the WPA key. Outputs an error message if\n   aircrack-ng has not been compiled with sqlite support.',font=self.myfont, bg="white", justify=LEFT).grid(row = 23, column = 2, padx = 5, pady = 5)
        
        self.C21 = Checkbutton(self.frame_content3, text = "-x/-x0", \
                 onvalue = "-x/-x0", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var21)
        self.C21.grid(row = 24, column = 0, padx = 5, pady = 5)
        self.t21=Text(self.frame_content3,height=1,width = 20)
        self.t21.grid(row = 24, column = 1, padx = 5, pady = 5)
        l21=Label(self.frame_content3, text = ':  (WEP cracking) Disable last keybytes brutforce.',font=self.myfont, bg="white", justify=LEFT).grid(row = 24, column = 2, padx = 5, pady = 5)
        
        
        #frame4
        Label(self.frame_content4, text = 'Aircrack-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        self.C22 = Checkbutton(self.frame_content4, text = "-x1", \
                 onvalue = "-x1", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var22)
        self.C22.grid(row = 25, column = 0, padx = 5, pady = 5)
        self.t22=Text(self.frame_content4,height=1,width = 20)
        self.t22.grid(row = 25, column = 1, padx = 5, pady = 5)
        l22=Label(self.frame_content4, text = ':  (WEP cracking) Enable last keybyte bruteforcing (default).',font=self.myfont, bg="white", justify=LEFT).grid(row = 25, column = 2, padx = 5, pady = 5)
        
        self.C23 = Checkbutton(self.frame_content4, text = "-x2", \
                 onvalue = "-x2", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var23)
        self.C23.grid(row = 26, column = 0, padx = 5, pady = 5)
        self.t23=Text(self.frame_content4,height=1,width = 20)
        self.t23.grid(row = 26, column = 1, padx = 5, pady = 5)
        l23=Label(self.frame_content4, text = ':  (WEP cracking) Enable last two keybytes bruteforcing.',font=self.myfont, bg="white", justify=LEFT).grid(row = 26, column = 2, padx = 5, pady = 5)
        
        self.C24 = Checkbutton(self.frame_content4, text = "-X", \
                 onvalue = "-X", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var24)
        self.C24.grid(row = 27, column = 0, padx = 5, pady = 5)
        self.t24=Text(self.frame_content4,height=1,width = 20)
        self.t24.grid(row = 27, column = 1, padx = 5, pady = 5)
        l24=Label(self.frame_content4, text = ':  (WEP cracking) Disable bruteforce multithreading (SMP only).',font=self.myfont, bg="white", justify=LEFT).grid(row = 27, column = 2, padx = 5, pady = 5)
        
        self.C25 = Checkbutton(self.frame_content4, text = "-y", \
                 onvalue = "-y", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var25)
        self.C25.grid(row = 28, column = 0, padx = 5, pady = 5)
        self.t25=Text(self.frame_content4,height=1,width = 20)
        self.t25.grid(row = 28, column = 1, padx = 5, pady = 5)
        l25=Label(self.frame_content4, text = ':  (WEP cracking) Experimental single bruteforce attack which\n   should only be used when the standard attack mode fails with\n   more than one million IVs',font=self.myfont, bg="white", justify=LEFT).grid(row = 28, column = 2, padx = 5, pady = 5)
        
        
        self.C26 = Checkbutton(self.frame_content4, text = "-u", \
                 onvalue = "-u", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var26)
        self.C26.grid(row = 29, column = 0, padx = 5, pady = 5)
        self.t26=Text(self.frame_content4,height=1,width = 20)
        self.t26.grid(row = 29, column = 1, padx = 5, pady = 5)
        l26=Label(self.frame_content4, text = ':  Long form -cpu-detect. Provide information on the number of\n   CPUs and MMX support. Example responses to "aircrack-ng \n   -cpu-detect" are "Nb CPU detected: 2" or Nb CPU detected: \n   1 (MMX available)".',font=self.myfont, bg="white", justify=LEFT).grid(row = 29, column = 2, padx = 5, pady = 5)
        
        self.C27 = Checkbutton(self.frame_content4, text = "-w", \
                 onvalue = "-w", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var27)
        self.C27.grid(row = 30, column = 0, padx = 5, pady = 5)
        self.t27=Text(self.frame_content4,height=1,width = 20)
        self.t27.grid(row = 30, column = 1, padx = 5, pady = 5)
        l27=Label(self.frame_content4, text = ':   (WPA cracking) Path to a wordlist or "-"without the quotes for \n    standard in (stdin).',font=self.myfont, bg="white", justify=LEFT).grid(row = 30, column = 2, padx = 5, pady = 5)
        
        self.C28 = Checkbutton(self.frame_content4, text = "-z", \
                 onvalue = "-z", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var28)
        self.C28.grid(row = 31, column = 0, padx = 5, pady = 5)
        self.t28=Text(self.frame_content4,height=1,width = 20)
        self.t28.grid(row = 31, column = 1, padx = 5, pady = 5)
        l28=Label(self.frame_content4, text = ':  Invokes the PTW WEP cracking method. (Default in v1.x)',font=self.myfont, bg="white", justify=LEFT).grid(row = 31, column = 2, padx = 5, pady = 5)
        
        #frame4
        Label(self.frame_content6, text = 'Aircrack-ng',font=self.headerfont, bg="white", padx=10, pady=10).grid(row = 0, column = 0)
        self.C29 = Checkbutton(self.frame_content6, text = "-P", \
                 onvalue = "-P", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var29)
        self.C29.grid(row = 32, column = 0, padx = 5, pady = 5)
        self.t29=Text(self.frame_content6,height=1,width = 20)
        self.t29.grid(row = 32, column = 1, padx = 5, pady = 5)
        l29=Label(self.frame_content6, text = ':  Long version -ptw-debug. Invokes the PTW debug mode.',font=self.myfont, bg="white", justify=LEFT).grid(row = 32, column = 2, padx = 5, pady = 5)
        
        self.C30 = Checkbutton(self.frame_content6, text = "-C", \
                 onvalue = "-C", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var30)
        self.C30.grid(row = 33, column = 0, padx = 5, pady = 5)
        self.t30=Text(self.frame_content6,height=1,width = 20)
        self.t30.grid(row = 33, column = 1, padx = 5, pady = 5)
        l30=Label(self.frame_content6, text = ':   Long version -combine. Merge the given APs to a virtual one.',font=self.myfont, bg="white", justify=LEFT).grid(row = 33, column = 2, padx = 5, pady = 5)
        
        self.C31 = Checkbutton(self.frame_content6, text = "-D", \
                 onvalue = "-D", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var31)
        self.C31.grid(row = 34, column = 0, padx = 5, pady = 5)
        self.t31=Text(self.frame_content6,height=1,width = 20)
        self.t31.grid(row = 34, column = 1, padx = 5, pady = 5)
        l31=Label(self.frame_content6, text = ':  Long version -wep-decloak. Run in WEP decloak mode.',font=self.myfont, bg="white", justify=LEFT).grid(row = 34, column = 2, padx = 5, pady = 5)
        
        self.C32 = Checkbutton(self.frame_content6, text = "-V", \
                 onvalue = "-V", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var32)
        self.C32.grid(row = 35, column = 0, padx = 5, pady = 5)
        self.t32=Text(self.frame_content6,height=1,width = 20)
        self.t32.grid(row = 35, column = 1, padx = 5, pady = 5)
        l32=Label(self.frame_content6, text = ':  Long version -visual-inspection. Run in visual inspection mode.',font=self.myfont, bg="white", justify=LEFT).grid(row = 35, column = 2, padx = 5, pady = 5)
        
        self.C33 = Checkbutton(self.frame_content6, text = "-1", \
                 onvalue = "-1", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var33)
        self.C33.grid(row = 36, column = 0, padx = 5, pady = 5)
        self.t33=Text(self.frame_content6,height=1,width = 20)
        self.t33.grid(row = 36, column = 1, padx = 5, pady = 5)
        l33=Label(self.frame_content6, text = ':  Long version -oneshot. Run in oneshot mode.',font=self.myfont, bg="white", justify=LEFT).grid(row = 36, column = 2, padx = 5, pady = 5)
        
        self.C34 = Checkbutton(self.frame_content6, text = "-S", \
                 onvalue = "-S", offvalue = "", height=1, \
                 bg="white", font=self.customFont,variable=self.var34)
        self.C34.grid(row = 37, column = 0, padx = 5, pady = 5)
        self.t34=Text(self.frame_content6,height=1,width = 20)
        self.t34.grid(row = 37, column = 1, padx = 5, pady = 5)
        l34=Label(self.frame_content6, text = ':  WPA cracking speed test.',font=self.myfont, bg="white", justify=LEFT).grid(row = 37, column = 2, padx = 5, pady = 5)
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
         
        listoutput=commands.getoutput("aircrack-ng"+" "+format(self.var1.get())+" "+(self.t1.get(1.0, 'end')).strip()+" "+format(self.var2.get())+" "+(self.t2.get(1.0, 'end')).strip()+" "+format(self.var3.get())+" "+(self.t3.get(1.0, 'end')).strip()+" "+format(self.var4.get())+" "+(self.t4.get(1.0, 'end')).strip()+" "+\
                            format(self.var5.get())+" "+(self.t5.get(1.0, 'end')).strip()+" "+format(self.var6.get())+" "+(self.t6.get(1.0, 'end')).strip()+" "+format(self.var7.get())+" "+(self.t7.get(1.0, 'end')).strip()+" "+format(self.var8.get())+" "+(self.t8.get(1.0, 'end')).strip()+" "+\
                            format(self.var9.get())+" "+(self.t9.get(1.0, 'end')).strip()+" "+format(self.var10.get())+" "+(self.t10.get(1.0, 'end')).strip()+" "+format(self.var11.get())+" "+(self.t11.get(1.0, 'end')).strip()+" "+format(self.var12.get())+" "+(self.t12.get(1.0, 'end')).strip()+" "+\
                            format(self.var13.get())+" "+(self.t13.get(1.0, 'end')).strip()+" "+format(self.var14.get())+" "+(self.t14.get(1.0, 'end')).strip()+" "+format(self.var15.get())+" "+(self.t15.get(1.0, 'end')).strip()+" "+format(self.var16.get())+" "+(self.t16.get(1.0, 'end')).strip()+" "+\
                            format(self.var17.get())+" "+(self.t17.get(1.0, 'end')).strip()+" "+format(self.var18.get())+" "+(self.t18.get(1.0, 'end')).strip()+" "+format(self.var19.get())+" "+(self.t19.get(1.0, 'end')).strip()+" "+format(self.var20.get())+" "+(self.t20.get(1.0, 'end')).strip()+" "+\
                            format(self.var21.get())+" "+ (self.t21.get(1.0, 'end')).strip()+" "+format(self.var22.get())+" "+(self.t22.get(1.0, 'end')).strip()+" "+format(self.var23.get())+" "+(self.t23.get(1.0, 'end')).strip()+" "+format(self.var24.get())+" "+(self.t24.get(1.0, 'end')).strip()+" "+\
                            format(self.var25.get())+" "+(self.t25.get(1.0, 'end')).strip()+" "+format(self.var26.get())+" "+(self.t26.get(1.0, 'end')).strip()+" "+format(self.var27.get())+" "+(self.t27.get(1.0, 'end')).strip()+" "+format(self.var28.get())+" "+(self.t28.get(1.0, 'end')).strip()+" "+format(self.var29.get())+" "+(self.t29.get(1.0, 'end')).strip()+" "+format(self.var30.get())+" "+(self.t30.get(1.0, 'end')).strip()+" "+format(self.var31.get())+" "+(self.t31.get(1.0, 'end')).strip()+" "+format(self.var32.get())+" "+(self.t32.get(1.0, 'end')).strip()+" "+format(self.var33.get())+" "+(self.t33.get(1.0, 'end')).strip()+" "+format(self.var34.get())+" "+(self.t34.get(1.0, 'end')).strip()+" "+listselection+" "+self.fname)  

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
