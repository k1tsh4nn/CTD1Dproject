import tkinter as tk
import time
import random
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class TextRotation():
    def __init__(self) -> None:
        self.output_text = [
            'Hello I am a robot, I do not like humans', 'OK', 'BYE']
        self.count = 0


class Avatar():
    def __init__(self, textbox, dialog) -> None:
        self.textbox = textbox
        self.dialog = dialog
        self.speaking = True

    def speak(self):
        return random.choice(self.dialog)


def main():
    pass
    mw.after(1000, main)


mw = tk.Tk()
canvas = tk.Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg='#ffff99')
canvas.pack()

man = tk.PhotoImage(file='images\png-men.png')
man = man.subsample(3)
canvas.create_image(0, SCREEN_HEIGHT, image=man, anchor='sw')

woman = tk.PhotoImage(file='images\png-girl.png')
woman = woman.subsample(4)
canvas.create_image(SCREEN_WIDTH, SCREEN_HEIGHT-150, image=woman, anchor='se')

HUD = canvas.create_rectangle(
    0, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT*2/4, fill='#e6f9ff')

canvas.focus_set()

guy = Avatar(canvas.create_text(0, SCREEN_HEIGHT*1/2,
             anchor='nw', text='Empty', font=('sans', 40), width=SCREEN_WIDTH/2), ['Hi', 'Hello', "You're so pretty", 'bye'])
girl = Avatar(canvas.create_text(SCREEN_WIDTH, SCREEN_HEIGHT *
              1/2, anchor='ne', text='Empty', font=('sans', 40), width=SCREEN_WIDTH/2), ['You are so disgusting', 'Bye', 'Cheers', 'Slay'])


def talk(A1: Avatar, A2: Avatar):
    if A1.speaking:
        text = A1.speak()
        canvas.itemconfig(A1.textbox, text=text)
        A1.speaking = False
        A2.speaking = True
    elif A2.speaking:
        text = A2.speak()
        canvas.itemconfig(A2.textbox, text=text)
        A2.speaking = False
        A1.speaking = True


def onClick(event: tk.Event):
    print(event.x, event.y)
    talk(guy, girl)


mw.bind("<Button-1>", onClick)

main()
mw.mainloop()
