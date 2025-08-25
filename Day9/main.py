from tkinter import *
window = Tk()
window.geometry("350x350")
window.title("Welcome Window")

e = Entry(window)
e.pack()

label = Label(window, text="Enter your name press the button")
label.pack()

def display():
   label['text'] = 'welcome to Tkinter '+e.get()

btn = Button(window, text="Click Me", command=display)
btn.pack()
window.mainloop()