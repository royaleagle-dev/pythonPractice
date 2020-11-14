#! python3
#itemizer.py --Automatically turn items in the clipboard to list items.
#idea: Al Sweigart
#Program: Ayotunde Okunubi

from pyperclip import copy, paste
import sys

to_be_listed = paste()
itemList = to_be_listed.split('\r\n')
finalList = ''

for items in itemList:
    finalList += f"* {items} \n"

copy(finalList)
