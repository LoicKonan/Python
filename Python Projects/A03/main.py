# # Import Required Library
# from tkinter import *

# from PyDictionary import PyDictionary

# # Create objects
# dictionary = PyDictionary()

# root = Tk()

# # Set geometry
# root.geometry("400X400")

# def dict():
#     meaning.config(text = dictionary.meaning(word.get())['Noun'][0])
#     meaning.config(text = dictionary.synonym(word.get()))
#     meaning.config(text = dictionary.antonym(word.get()))
    
# # Add Labels, Button and Frames
# Label(root, text = "Dictionary", font = ("Helvetica 20 bold"), fg = "Green").pack( pady = 10)

# # Frame 1st
# frame = Frame(root)
# Label(frame, text = "Type Word", font = ("Helvetica 15 bold")).pack(side = LEFT)

# word = Entry(frame, font = ("Helvetica 15 bold"))

# word.pack()
# frame.pack( pady = 10)

# # Frame 2nd
# frame1 = Frame(root)
# Label(frame1, text = "Meaning:- ", font = ("Helvetica 10 bold")).pack(side = LEFT)
# meaning = Label(frame1, text = "", font = ("Helvetica 10 bold"))
# meaning.pack()
# frame1.pack(pady = 10)


# # Frame 3rd
# frame2 = Frame(root)
# Label(frame2, text = "Synonym:- ", font= ("Helvetica 10 bold").pack(side = LEFT))
# synonym = Label(frame2, text = "", font = ("Helvetica 10"))
# synonym.pack()
# frame2.pack( pady = 10)


# # Frame 4th
# frame3 = Frame(root)
# Label(frame3, text = "Meaning:- ", font = ("Helvetica 10 bold")).pack(side = LEFT)
# antonym = Label(frame3, text = "", font = ("Helvetica 10"))
# antonym.pack(side = LEFT)
# frame3.pack(pady = 10)
# Button(root, text = "Submit", font = ("Helvetica 15 bold"), conmmand = dict).pack()


# # Execute Tkinter 
# root.mainloop()

import tkinter
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


#create main window
master = tkinter.Tk()
master.title("tester")
master.geometry("300x100")


#make a label for the window
label1 = tkinter.Label(master, text='Hellooooo')
# Lay out label
label1.pack()

# Run forever!
master.mainloop()