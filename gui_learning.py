from tkinter import *

## main:

window = Tk()
window.title("My Glossary")
window.configure(background="black")

## My Label
Label (window, text = "tic tac toe", bg="white", fg = "white", font="none") .grid(row=3, column=0, sticky=W)


## run the main loop
window.mainloop()
