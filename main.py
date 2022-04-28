from tkinter import *


# Button
def button_clicked():
    # input.get() gets input inside text entry field
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New text"
my_label.config(text="New Text", padx=50, pady=50)
# makes label appear on screen - won't appear without .pack()
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# use command to run functions
button = Button(text="Click Me", command=button_clicked)
new_button = Button(text="New Button")
# button.pack()
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
