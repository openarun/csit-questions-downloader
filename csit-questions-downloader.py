#!/usr/bin/env python

#MIT License

#Copyright (c) 2016 Arun Pyasi

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import sys
from subprocess import call

def download():
	for year in range(2065,2070):
		call(["mkdir", selected])
		call(["wget","https://ia902601.us.archive.org/27/items/bio-2066/"+str(selected)+"-"+str(year)+".pdf", "-P", selected])
		print("Successfully downloaded "+str(selected)+"-"+str(year))
	print "Good Luck ! This project is open source and is written in python by Arun."
	print "===============github.com/arunpyasi/csit-question-downloader=============="
	print "Written in basic Python language" 

print "+++Welcome to CSIT Old is Gold CLI based Downloader+++"
sem = input("Enter the semester number you wanna download : ")
print "Select the subject to download for "+str(sem)+" Semester"

if sem == 2:
	print "0. DSA"
	print "1. DL"
	print "2. MP"
	print "3. LA"
	print "4. STAT-II"
	print "5. DS"
	print "6. ALL"
else:
	print "Get the hell out of here"

subno = input("Enter the subject here.")
subdata = ["dsa", "dl", "mp", "la", "sta", "ds", "all"]
if subno == 6:
	for all in range(0,6):
		selected = str(subdata[all])
		download()
else:
	selected = str(subdata[subno])
	download()
