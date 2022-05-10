import tkinter as tk

def click(event) :
    label.configure(text=(event.x,event.y))

window = tk.Tk()

window.title("hello_tuto")
window.geometry("500x500")
window.resizable(width=False, height=False)

label = tk.Label(window, font=("",30), fg="orange")

window.bind("<Button-1>",click)

label.pack(side="left")


window.mainloop()
