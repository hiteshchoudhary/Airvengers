#!/bin/bash

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#     Script to make all files executable at once. Also this will run base GUI file for project                                          #
#       Project is based on Aircrack-ng set of tools and is specially designed to run on KALI LINUX.                                     #
#                                                                                                                                        # 
#              Designed by : Hitesh Choudhary                                                                                            #
#              Home page   : www.HiteshChoudhary.com                                                                                     #
#              Email       : hitesh@hiteshchoudhary.com                                                                                  #
#              Based on    : www.Aircrack-ng.org                                                                                         #
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

chmod 755 Aigraph-ng.py Airdecloak-ng.py Airodump-ng.py AirvengersGUI.py Airbase-ng.py Airdrop-ng.py Airolib-ng.py Aircrack-ng.py Aireplay-ng.py Airserv-ng.py Airdecap-ng.py Airmon-ng.py Airtun-ng.py;
python AirvengersGUI.py
