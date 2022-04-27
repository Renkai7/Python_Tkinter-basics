from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# makes label appear on screen - won't appear without .pack()
my_label.pack()

my_label["text"] = "New text"
# my_label.config(text="New Text")

# Button
button = Button(text="Click Me")
button.pack()

window.mainloop()
