from tkinter import *
root = Tk()
e = Entry(root)
e.grid(row=5, column=0, columnspan=2)
def onclick():
    clickedLabel = Label(root, text="You Clicked Me!!")
    clickedLabel.grid(row=2, column=0)
myLabel = Label(root, text="Welcome in Cusine control")
firstButton = Button(root, text="Click Me", command= onclick, bg="green", fg="white")
myLabel.grid(row=0, column=0)
firstButton.grid(row=1, column=0)


root.mainloop()

#Final Commit
