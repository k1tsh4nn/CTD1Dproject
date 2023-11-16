import tkinter as tk

mw = tk.Tk()
canvas = tk.Canvas(width=500,height=500)
canvas.pack()

dialog = 'Hello Im blah'

for i in range(20):
    textwidget = canvas.create_text(100,100+i*20,text=dialog)
mw.mainloop()   