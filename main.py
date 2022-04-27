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
def button_clicked():
    # input.get() gets input inside text entry field
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked")

# use command to run functions
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()



window.mainloop()
