#! python3
#mclip.py - A multi-clipboard program

TEXT = {
    'agree': """Yes I agree. That sounds fine to me.""",
    'busy': """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""
    }

import sys
from pyperclip import copy, paste

if len(sys.argv)<2:
    print('Usage: python mclip.py [keyphrase] -copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]     #first comand line arg is the keyphrase

if keyphrase in TEXT:
    copy(TEXT[keyphrase])
    print ("Text for" + keyphrase + " copied to clipboard.")
else:
    print('There isno text for ' + keyphrase)



"""
Note, the sys.argv stores command line arguments. The first item in the ssys.argv list
i.e. sys.argv[0] should be the filename, and the
second item should be the first command line argument.
Thus it is imperative to test whether items in the sys.argv is not less than 2.
"""
