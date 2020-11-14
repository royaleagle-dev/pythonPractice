import os
import time
import sys
import PySimpleGUI as sg

directory = r"C:\pythonProgramming"

if len(sys.argv) == 1:
	directory = sg.popup_get_folder('Please enter folder')
	if not directory:
		sg.popup_error("You did not enter anything")
		exit()
else:
	directory = sys.argv[1]

files = os.listdir(directory)
sg.popup_scrolled('\n'.join(files))


#notes
"""
Join works on iterables

Print("items") #print with the capital 'P' outputs to a debug window in pysimplegui
example:
Print(files)
"""