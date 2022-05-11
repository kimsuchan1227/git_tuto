import tkinter as tk
import tkinter.messagebox as mbox
import tkinter.simpledialog as sim

def click(event) :
    mbox.showinfo("",(event.x,event.y))

window = tk.Tk()

window.title("hello_tuto")
window.geometry("500x500")
window.resizable(width=False, height=False)

window.bind("<Button-1>",click)

sim.askinteger("","number",maxvalue=10)

tk.Label(text="Hello", font=("",30), fg="orange").pack(side="left")

window.mainloop()
