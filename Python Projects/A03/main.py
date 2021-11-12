# Import Required Library

from tkinter import*

from PyDictionary import PyDictionary

# Create objects

dictionary = PyDictionary()

root = Tk()

# Set geometry

root.geometry("400X400")

def dict():
    meaning.config(text = dictionary.meaning(word.get())['Noun'][0])
    meaning.config(text = dictionary.meaning(synonym.get()))
    meaning.config(text = dictionary.meaning(anton.get()))
    
# Add Labels, Button and Frames
Label(root, text = "Dictionary", font = ("Helvetica 20 bold"), fg = "Green").pack( pady = 10)

# Frame 1
frame = Frame(root)
Label(frame, text = "Type Word", font = ("Helvetica 15 bold")).pack(side = LEFT)

WORD = Entry(frame, font = ("Helvetica 15 bold"))

word.pack()
frame.pack( pady = 10)

