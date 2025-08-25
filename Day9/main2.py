from tkinter import *
window = Tk()
window.geometry("350x350")
window.title("Addition Window")
e1 = Entry(window)
e1.pack()
e2 = Entry(window)
e2.pack()
label = Label(window, text="Result Appears here")
label.pack()
def addition():
    n1 = float(e1.get())
    n2 = float(e2.get())
    ans = n1 + n2
    label['text'] = str(ans)
btn = Button(window, text="Click Me", command=addition)
btn.pack()
window.mainloop()