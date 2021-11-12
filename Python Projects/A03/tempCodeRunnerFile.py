# Import Required Library

from tkinter import*
from tkinter import font

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

# Frame 1st
frame = Frame(root)
Label(frame, text = "Type Word", font = ("Helvetica 15 bold")).pack(side = LEFT)

WORD = Entry(frame, font = ("Helvetica 15 bold"))

word.pack()
frame.pack( pady = 10)

# Frame 2nd
frame1 = Frame(root)
Label(frame1, text = "Meaning:- ", font = ("Helvetica 10 bold")).pack(side = LEFT)
meaning = Label(frame1, text = "", font = ("Helvetica 10 bold"))
meaning.pack()
frame1.pack(pady = 10)

# Frame 3rd
frame2 = Frame(root)
Label(frame2, text = "Synonym:- ", font= ("Helvetica 10 bold").pack(side = LEFT))
synonym = Label(frame2, text = "", font = ("Helvetica 10"))
synonym.pack()
frame2.pack( pady = 10)

# Frame 4th

frame1 = Frame(root)
Label(frame1, text = "Meaning:- ", font = ("Helvetica 10 bold")).pack(side = LEFT)
meaning = Label(frame1, text = "", font = ("Helvetica 10 bold"))
meaning.pack()
frame1.pack(pady = 10)

# Frame 3rd
frame2 = Frame(root)
Label(frame2, text = "Synonym:- ", font= ("Helvetica 10 bold").pack(side = LEFT))
synonym = Label(frame2, text = "", font = ("Helvetica 10"))
synonym.pack()
frame2.pack( pady = 10)

# Execute Tkinter 
root.mainloop()

