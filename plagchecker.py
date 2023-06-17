import difflib
import os
import _tkinter
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

os.system('cls');

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

print("Select first file")
filename1 = askopenfilename() # show an "Open" dialog box and return the path to the selected file

print("Select second file")
filename2 = askopenfilename() # show an "Open" dialog box and return the path to the selected file

with open(filename1) as doc1, open(filename2) as doc2:
    fil1data = doc1.read()
    file2data = doc2.read()
    calculate_similarity = difflib.SequenceMatcher(None, fil1data, file2data).ratio()
    print(f'Plag percent between File1 and File2 is : {calculate_similarity*100}%')