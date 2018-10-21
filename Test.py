import sys
import os
import tkinter as tk

root = tk.Tk()

def helloCallBack():
    os.system('CSVParse.py')
    #Keep_both_files_in_the_same_Folder
    b1=tk.Button(root, text="Calendar",bg="white",command=helloCallBack)
    b1.pack()
    root.mainloop()