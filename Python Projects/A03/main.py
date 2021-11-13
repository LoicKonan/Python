from tkinter import *

fL = {}

def commando(x, y):
    fL.update({x:int(y)})  # Please note that these x and y vars are private to this function.  They are not the x and y vars as defined below.
    print(fL)

root = Tk()
root.title("Spam Words")

x = StringVar()  # Creating the variables that will get the user's input.
y = StringVar()

label_1 = Label(root, text="Say a word: ", bg="#333333", fg="white")
label_2 = Label(root, text="Give it a value, 1-10:", bg="#333333", fg="white")
entry_1 = Entry(root, textvariable=x)
entry_2 = Entry(root, textvariable=y)

label_1.grid(row=1)
label_2.grid(row=3)

entry_1.grid(row=2, column=0)
entry_2.grid(row=4, column=0)

but = Button(root, text="Execute", bg="#333333", fg="white", command=lambda :commando(x.get(), y.get()))  # Note the use of lambda and the x and y variables.
but.grid(row=5, column=0)

root.mainloop()